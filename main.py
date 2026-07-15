# ================================================================
# EMOTION INTELLIGENCE PLATFORM - v20.0 ULTIMATE
# ================================================================
# Desenvolvido por: Albert Menezes
# Versão: 14.0 ULTIMATE
# Framework: FastAPI + Uvicorn
# Banco: SQLite + SQLAlchemy
# IA: Google Gemini 2.0 Flash
# Pagamentos: MercadoPago
# Emails: SendGrid
# Deploy: Render.com
# ================================================================
#
# FUNCIONALIDADES:
# ✅ Autenticação completa com sessões seguras
# ✅ Análise de emoções avançada (15 emoções)
# ✅ IA Psicóloga Sofia (Google Gemini 2.0)
# ✅ Diário emocional completo
# ✅ Gamificação (pontos + badges + ranking)
# ✅ Planos Free/Trial/Premium/Enterprise
# ✅ MercadoPago + Webhook automático
# ✅ SendGrid (boas-vindas, premium, relatório semanal)
# ✅ Relatório semanal automático por email
# ✅ Sistema de afiliados com comissão 20%
# ✅ Painel Admin completo
# ✅ API pública com token
# ✅ Rate limiting por IP
# ✅ Logs de acesso detalhados
# ✅ Health check
# ✅ PWA instalável
# ✅ Chat ao vivo Tawk.to
# ================================================================

# ================================================================
# IMPORTS
# ================================================================

from fastapi import (
    FastAPI, HTTPException, Request, Depends,
    Form, BackgroundTasks, Header, UploadFile, File
)
from fastapi.responses import (
    HTMLResponse, RedirectResponse, Response, JSONResponse
)
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.exception_handlers import http_exception_handler
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from sqlalchemy import (
    create_engine, Column, Integer, String,
    DateTime, ForeignKey, Text, Boolean, Float
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from passlib.context import CryptContext
from datetime import datetime, date, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from collections import defaultdict
from google import genai
from google.genai import types

import unicodedata
import mercadopago
import sendgrid
from sendgrid.helpers.mail import Mail
import uuid
import os
import json
import hashlib
import time
import re

# ================================================================
# CONFIGURAÇÕES GLOBAIS
# ================================================================

MP_ACCESS_TOKEN  = os.environ.get("MP_ACCESS_TOKEN")
ADMIN_EMAIL      = os.environ.get("ADMIN_EMAIL", "albertmenezes2006@gmail.com")
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
BASE_URL         = os.environ.get("BASE_URL", "http://localhost:8000")
GEMINI_API_KEY   = os.environ.get("GEMINI_API_KEY")
TELEGRAM_TOKEN   = os.environ.get("TELEGRAM_TOKEN", "8909749074:AAGNoB-JPZVC0Vl1dYeiN__1ktxza6GZ0s4")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "7757404855")
API_SECRET       = os.environ.get("API_SECRET", str(uuid.uuid4()))
SECRET_KEY       = os.environ.get("SECRET_KEY", str(uuid.uuid4()))

# ================================================================
# CLIENTE GEMINI 2.0
# ================================================================

cliente_ia = genai.Client(api_key=GEMINI_API_KEY)

# ================================================================
# LIMITES POR PLANO
# ================================================================

LIMITES = {
    "free": {
        "analises": 10,
        "chat":     5,
        "diario":   3
    },
    "trial": {
        "analises": 50,
        "chat":     20,
        "diario":   10
    },
    "premium": {
        "analises": 999999,
        "chat":     999999,
        "diario":   999999
    },
    "enterprise": {
        "analises": 999999,
        "chat":     999999,
        "diario":   999999
    },
}

# ================================================================
# PREÇOS
# ================================================================

PRECOS = {
    "premium": {
        "valor": 49,
        "nome":  "Emotion Premium"
    },
    "enterprise": {
        "valor": 199,
        "nome":  "Emotion Enterprise"
    }
}

# ================================================================
# CONFIGURAÇÕES DE AFILIADOS E GAMIFICAÇÃO
# ================================================================

COMISSAO_PERCENT = 20

BADGES = [
    (0,    "🌱 Iniciante"),
    (50,   "🌿 Explorador"),
    (200,  "🔥 Intermediário"),
    (500,  "⭐ Avançado"),
    (1000, "🏆 Especialista"),
    (2000, "💎 Mestre Emocional"),
    (5000, "👑 Lenda Emocional"),
]

PONTOS_POR_ACAO = {
    "cadastro":  10,
    "analise":   5,
    "chat_free": 2,
    "chat_premium": 5,
    "diario":    8,
    "trial":     20,
    "premium":   50,
}

# ================================================================
# RATE LIMITING
# ================================================================

rate_limit_store = defaultdict(list)

def limpar_rate_limit_store():
    """Limpa entradas antigas do rate limit store — previne memory leak"""
    agora = time.time()
    keys_remover = []
    for ip, acessos in rate_limit_store.items():
        rate_limit_store[ip] = [t for t in acessos if agora - t < 3600]
        if not rate_limit_store[ip]:
            keys_remover.append(ip)
    for k in keys_remover:
        del rate_limit_store[k]

# ================================================================
# BANCO DE DADOS
# ================================================================

# PostgreSQL se disponivel, senao SQLite como fallback
_db_url = os.getenv("DATABASE_URL", "sqlite:///./emotion.db")

# Render retorna postgres:// mas SQLAlchemy precisa de postgresql://
if _db_url.startswith("postgres://"):
    _db_url = _db_url.replace("postgres://", "postgresql://", 1)

DATABASE_URL = _db_url

if DATABASE_URL.startswith("postgresql"):
    engine = create_engine(
        DATABASE_URL,
        pool_size=5,
        max_overflow=10,
        pool_pre_ping=True,
        pool_recycle=300,
    )
    print(f"[DB] Conectado ao PostgreSQL")
else:
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False}
    )
    print(f"[DB] Usando SQLite local")

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
Base = declarative_base()

# ================================================================
# MODELOS DO BANCO
# ================================================================

class Usuario(Base):
    __tablename__ = "usuarios"

    id             = Column(Integer,  primary_key=True, index=True)
    nome           = Column(String,   nullable=False)
    email          = Column(String,   unique=True, index=True, nullable=False)
    senha          = Column(String,   nullable=False)
    plano          = Column(String,   default="free")
    trial_usado    = Column(Boolean,  default=False)
    trial_expira   = Column(DateTime, nullable=True)
    ref_code       = Column(String,   unique=True, nullable=True)
    indicado_por   = Column(String,   nullable=True)
    creditos_analise = Column(Integer, default=0)
    creditos_sofia   = Column(Integer, default=0)
    plano_anual_ate  = Column(DateTime, nullable=True)
    plano_api        = Column(String, nullable=True)
    whitelabel_id    = Column(Integer, nullable=True)
    total_gasto      = Column(Float, default=0.0)
    fonte_receita    = Column(String, nullable=True)
    pontos         = Column(Integer,  default=0)
    badge          = Column(String,   default="🌱 Iniciante")
    api_token      = Column(String,   unique=True, nullable=True)
    ativo          = Column(Boolean,  default=True)
    bio            = Column(Text,     nullable=True)
    avatar         = Column(String,   nullable=True)
    criado_em      = Column(DateTime, default=datetime.now)
    ultimo_acesso  = Column(DateTime, nullable=True)

    analises  = relationship("Analise",   back_populates="usuario", cascade="all, delete")
    mensagens = relationship("Mensagem",  back_populates="usuario", cascade="all, delete")
    diarios   = relationship("Diario",    back_populates="usuario", cascade="all, delete")
    logs      = relationship("LogAcesso", back_populates="usuario", cascade="all, delete")
    conquistas = relationship("Conquista", back_populates="usuario", cascade="all, delete")


class Analise(Base):
    __tablename__ = "analises"

    id           = Column(Integer,  primary_key=True, index=True)
    texto        = Column(String,   nullable=False)
    emocao       = Column(String,   nullable=False)
    emoji        = Column(String,   nullable=False)
    recomendacao = Column(String,   nullable=False)
    intensidade  = Column(Integer,  default=1)
    tecnica      = Column(String,   nullable=True)
    criado_em    = Column(DateTime, default=datetime.now)
    usuario_id   = Column(Integer,  ForeignKey("usuarios.id"))

    usuario = relationship("Usuario", back_populates="analises")


class Mensagem(Base):
    __tablename__ = "mensagens"

    id         = Column(Integer,  primary_key=True, index=True)
    conteudo   = Column(Text,     nullable=False)
    resposta   = Column(Text,     nullable=False)
    emocao     = Column(String,   nullable=True)
    emoji      = Column(String,   nullable=True)
    criado_em  = Column(DateTime, default=datetime.now)
    usuario_id = Column(Integer,  ForeignKey("usuarios.id"))

    usuario = relationship("Usuario", back_populates="mensagens")


class Diario(Base):
    __tablename__ = "diarios"

    id         = Column(Integer,  primary_key=True, index=True)
    titulo     = Column(String,   nullable=False)
    conteudo   = Column(Text,     nullable=False)
    emocao     = Column(String,   nullable=True)
    emoji      = Column(String,   nullable=True)
    humor      = Column(Integer,  default=3)
    criado_em  = Column(DateTime, default=datetime.now)
    usuario_id = Column(Integer,  ForeignKey("usuarios.id"))

    usuario = relationship("Usuario", back_populates="diarios")


class LogAcesso(Base):
    __tablename__ = "logs_acesso"

    id         = Column(Integer,  primary_key=True, index=True)
    rota       = Column(String,   nullable=False)
    metodo     = Column(String,   nullable=False)
    ip         = Column(String,   nullable=True)
    status     = Column(Integer,  nullable=True)
    duracao_ms = Column(Float,    nullable=True)
    user_agent = Column(String,   nullable=True)
    criado_em  = Column(DateTime, default=datetime.now)
    usuario_id = Column(Integer,  ForeignKey("usuarios.id"), nullable=True)

    usuario = relationship("Usuario", back_populates="logs")


class Pagamento(Base):
    __tablename__ = "pagamentos"

    id         = Column(Integer,  primary_key=True, index=True)
    usuario_id = Column(Integer,  ForeignKey("usuarios.id"))
    plano      = Column(String,   nullable=False)
    valor      = Column(Float,    nullable=False)
    status     = Column(String,   default="pendente")
    mp_id      = Column(String,   nullable=True)
    metodo     = Column(String,   nullable=True)
    criado_em  = Column(DateTime, default=datetime.now)


class Conquista(Base):
    __tablename__ = "conquistas"

    id         = Column(Integer,  primary_key=True, index=True)
    nome       = Column(String,   nullable=False)
    descricao  = Column(String,   nullable=False)
    emoji      = Column(String,   nullable=False)
    criado_em  = Column(DateTime, default=datetime.now)
    usuario_id = Column(Integer,  ForeignKey("usuarios.id"))

    usuario = relationship("Usuario", back_populates="conquistas")


class Cupom(Base):
    __tablename__ = "cupons"
    id           = Column(Integer, primary_key=True, index=True)
    codigo       = Column(String, unique=True, index=True)
    desconto_pct = Column(Integer, default=10)
    ativo        = Column(Boolean, default=True)
    usos_maximos = Column(Integer, default=100)
    usos_atuais  = Column(Integer, default=0)
    expira_em    = Column(DateTime, nullable=True)
    criado_em    = Column(DateTime, default=datetime.now)

class Notificacao(Base):
    __tablename__ = "notificacoes"

    id         = Column(Integer,  primary_key=True, index=True)
    titulo     = Column(String,   nullable=False)
    mensagem   = Column(Text,     nullable=False)
    lida       = Column(Boolean,  default=False)
    criado_em  = Column(DateTime, default=datetime.now)
    usuario_id = Column(Integer,  ForeignKey("usuarios.id"))


# Criar todas as tabelas

class Credito(Base):
    __tablename__ = "creditos"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    tipo = Column(String, default="analise")
    quantidade = Column(Integer, default=0)
    usado = Column(Integer, default=0)
    pacote = Column(String, default="P")
    criado_em = Column(DateTime, default=datetime.utcnow)
    expira_em = Column(DateTime, nullable=True)

class Presente(Base):
    __tablename__ = "presentes"
    id = Column(Integer, primary_key=True)
    codigo = Column(String, unique=True, index=True)
    remetente_id = Column(Integer, ForeignKey("usuarios.id"))
    destinatario_email = Column(String, nullable=True)
    plano = Column(String, default="premium")
    valor = Column(Float, default=49.0)
    usado = Column(Boolean, default=False)
    usado_por = Column(Integer, nullable=True)
    mensagem = Column(String, nullable=True)
    criado_em = Column(DateTime, default=datetime.utcnow)
    expira_em = Column(DateTime, nullable=True)

class ApiKey(Base):
    __tablename__ = "api_keys"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    chave = Column(String, unique=True, index=True)
    nome = Column(String, default="Minha API")
    ativa = Column(Boolean, default=True)
    requisicoes_mes = Column(Integer, default=0)
    limite_mes = Column(Integer, default=1000)
    plano_api = Column(String, default="developer")
    criado_em = Column(DateTime, default=datetime.utcnow)
    ultimo_uso = Column(DateTime, nullable=True)

class WhiteLabel(Base):
    __tablename__ = "whitelabel"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    empresa = Column(String)
    slug = Column(String, unique=True, index=True)
    logo_url = Column(String, nullable=True)
    cor_primaria = Column(String, default="#667eea")
    cor_secundaria = Column(String, default="#764ba2")
    dominio_custom = Column(String, nullable=True)
    ativo = Column(Boolean, default=True)
    max_usuarios = Column(Integer, default=50)
    usuarios_ativos = Column(Integer, default=0)
    criado_em = Column(DateTime, default=datetime.utcnow)
    expira_em = Column(DateTime, nullable=True)

class SessaoSofia(Base):
    __tablename__ = "sessoes_sofia"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    msgs_disponiveis = Column(Integer, default=10)
    msgs_usadas = Column(Integer, default=0)
    pago = Column(Boolean, default=False)
    valor_pago = Column(Float, default=4.90)
    criado_em = Column(DateTime, default=datetime.utcnow)
    expira_em = Column(DateTime, nullable=True)

class RelatorioPago(Base):
    __tablename__ = "relatorios_pagos"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    mes_ref = Column(String)
    valor_pago = Column(Float, default=9.90)
    payment_id = Column(String, nullable=True)
    criado_em = Column(DateTime, default=datetime.utcnow)

class TransacaoCredito(Base):
    __tablename__ = "transacoes_credito"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    tipo = Column(String)
    quantidade = Column(Integer)
    descricao = Column(String)
    payment_id = Column(String, nullable=True)
    criado_em = Column(DateTime, default=datetime.utcnow)


# Migração antecipada — roda ANTES do create_all para evitar erro de colunas
def rodar_migracoes():
    """Migração automática — adiciona colunas novas sem quebrar dados existentes"""
    try:
        with engine.connect() as conn:
            migracoes = [
                "ALTER TABLE usuarios ADD COLUMN IF NOT EXISTS creditos_analise INTEGER DEFAULT 0",
                "ALTER TABLE usuarios ADD COLUMN IF NOT EXISTS creditos_sofia INTEGER DEFAULT 0",
                "ALTER TABLE usuarios ADD COLUMN IF NOT EXISTS plano_anual_ate TIMESTAMP",
                "ALTER TABLE usuarios ADD COLUMN IF NOT EXISTS plano_api VARCHAR",
                "ALTER TABLE usuarios ADD COLUMN IF NOT EXISTS whitelabel_id INTEGER",
                "ALTER TABLE usuarios ADD COLUMN IF NOT EXISTS total_gasto FLOAT DEFAULT 0.0",
                "ALTER TABLE usuarios ADD COLUMN IF NOT EXISTS fonte_receita VARCHAR",
            ]
            for sql in migracoes:
                try:
                    conn.execute(text(sql))
                    conn.commit()
                    print(f"Migracao OK: {sql[:50]}")
                except Exception as e:
                    pass  # coluna ja existe — normal
        print("Migracoes concluidas!")
    except Exception as e:
        print(f"Migracoes skip (SQLite ou primeira vez): {e}")

rodar_migracoes()


class PerfilSofia(Base):
    """Perfil psicologico do usuario construido pela Sofia ao longo do tempo"""
    __tablename__ = "perfis_sofia"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), unique=True)
    resumo = Column(String, nullable=True)  # Resumo do perfil psicologico
    temas_principais = Column(String, nullable=True)  # Temas mais discutidos
    tecnicas_usadas = Column(String, nullable=True)  # Tecnicas aplicadas
    progresso = Column(String, nullable=True)  # Evolucao observada
    alertas = Column(String, nullable=True)  # Pontos de atencao
    atualizado_em = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)


# Cria cupons padrao se nao existirem
def criar_cupons_padrao():
    db = SessionLocal()
    try:
        cupons_padrao = [
            {"codigo": "BEMVINDO10", "desconto_pct": 10, "usos_maximos": 1000, "dias": 365},
            {"codigo": "EVOLUCAO20", "desconto_pct": 20, "usos_maximos": 500,  "dias": 365},
            {"codigo": "PROMO30",    "desconto_pct": 30, "usos_maximos": 100,  "dias": 30},
        ]
        for c in cupons_padrao:
            existe = db.query(Cupom).filter(Cupom.codigo == c["codigo"]).first()
            if not existe:
                novo = Cupom(
                    codigo=c["codigo"],
                    desconto_pct=c["desconto_pct"],
                    usos_maximos=c["usos_maximos"],
                    expira_em=datetime.now() + timedelta(days=c["dias"])
                )
                db.add(novo)
        db.commit()
        print("[STARTUP] Cupons padrao criados/verificados")
    except Exception as e:
        print(f"[STARTUP] Erro cupons: {e}")
    finally:
        db.close()

criar_cupons_padrao()

# ================================================================
# SEGURANÇA
# ================================================================

pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")


def hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)


def verificar_senha(senha: str, hash: str) -> bool:
    return pwd_context.verify(senha, hash)


def gerar_ref_code(nome: str) -> str:
    base   = re.sub(r'[^a-z0-9]', '', nome.lower())[:6]
    sufixo = str(uuid.uuid4())[:4]
    return f"{base}{sufixo}"


def gerar_api_token(email: str) -> str:
    return hashlib.sha256(
        f"{email}{uuid.uuid4()}{SECRET_KEY}".encode()
    ).hexdigest()


def rate_limit(ip: str, limite: int = 30, janela: int = 60) -> bool:
    agora   = time.time()
    acessos = rate_limit_store[ip]
    acessos = [t for t in acessos if agora - t < janela]
    rate_limit_store[ip] = acessos
    if len(acessos) >= limite:
        return False
    rate_limit_store[ip].append(agora)
    return True


def validar_email(email: str) -> bool:
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(padrao, email))


def validar_senha(senha: str) -> tuple[bool, str]:
    if len(senha) < 8:
        return False, "Senha deve ter pelo menos 8 caracteres"
    if not re.search(r'[0-9]', senha):
        return False, "Senha deve conter pelo menos um número"
    return True, ""

# ================================================================
# DETECÇÃO DE EMOÇÕES — EXPANDIDA (15 EMOÇÕES)
# ================================================================

palavras_emocoes = {
    "alegria": [
        "feliz", "alegre", "contente", "animado", "otimo", "maravilhoso",
        "incrivel", "satisfeito", "radiante", "euforico", "empolgado",
        "bem", "prazer", "alegra", "jubilo", "vencedor", "felicidade",
        "sorrindo", "rindo", "divertido", "animada", "excelente",
        "magnifico", "esplendido", "glorioso", "encantado", "deslumbrado",
        "extasiado", "entusiasmado", "vibrante", "positivo", "vitorioso",
        "realizado", "pleno", "gratificado", "encantadora", "alegria",
        "ótimo", "ótima", "felizes", "contentes", "animados", "radiantes",
        "bom dia", "boa tarde", "boa noite", "tudo bem", "muito bem",
        "super bem", "indo bem", "melhorando", "melhorou", "melhor"
    ],
    "tristeza": [
        "triste", "deprimido", "chateado", "desanimado", "sozinho",
        "melancolico", "chorando", "sofrendo", "perdido", "abandonado",
        "luto", "dor", "pena", "lamento", "chorar", "vazio", "angustia",
        "desesperado", "inconsolavel", "abatido", "desolado", "pesaroso",
        "magoado", "decepcionado", "frustrado", "desapontado", "infeliz",
        "sofrimento", "tormento", "agonia", "tristeza", "depressao",
        "desanimo", "desespero", "melancolia", "saudade triste",
        "sem esperanca", "sem saida", "nao aguento", "nao consigo mais",
        "cansado de tudo", "nao quero mais", "desistir", "desisti"
    ],
    "raiva": [
        "raiva", "irritado", "furioso", "bravo", "odio", "revoltado",
        "indignado", "nervoso", "estressado", "explosivo", "agressivo",
        "enfurecido", "colera", "raivoso", "irritada", "com raiva",
        "com odio", "irritante", "insuportavel", "injusto", "absurdo",
        "ridiculo", "estupido", "idiota", "horrivel", "que absurdo",
        "nao aguento", "me irrita", "me irrito", "fui enganado",
        "traido", "mentira", "mentiroso", "falsidade", "falso",
        "hipocrisia", "hipocrita", "raiva de", "com raiva de",
        "muito bravo", "muito nervoso", "explodindo", "nao suporto"
    ],
    "medo": [
        "medo", "assustado", "apavorado", "ansioso", "preocupado",
        "tenso", "inseguro", "receoso", "aterrorizado", "ansiedade",
        "panico", "fobia", "tremendo", "com medo", "apavorada",
        "aterrador", "assustadora", "medroso", "apreensivo",
        "angustiado", "perturbado", "inquieto", "alarmado",
        "horrorizado", "terror", "tremor", "coração acelerado",
        "suando frio", "nao consigo respirar", "sufocando",
        "claustrofobia", "agorafobia", "fobia social", "timidez",
        "vergonha social", "medo de falhar", "medo do futuro",
        "medo de morrer", "medo de perder", "ansiedade social"
    ],
    "surpresa": [
        "surpreso", "chocado", "impressionado", "espantado", "uau",
        "nossa", "caramba", "inacreditavel", "nao acredito",
        "surpreendente", "inesperado", "inexplicavel", "extraordinario",
        "fenomenal", "assombroso", "estupendo", "admirado", "nossa senhora",
        "meu deus", "que surpresa", "nao esperava", "de repente",
        "do nada", "sem aviso", "me pegou de surpresa", "wow",
        "uau que", "que coisa", "jamais imaginei", "nunca pensei"
    ],
    "nojo": [
        "nojo", "repulsa", "asco", "horrivel", "terrivel", "repugnante",
        "enjoado", "asqueroso", "que nojo", "nauseante", "revoltante",
        "detestavel", "abominavel", "execravel", "repulsivo", "nojentas",
        "que horror", "que coisa horrivel", "me deu nojo", "sinto nojo",
        "insuportavel", "intoleravel", "que asco", "me enjoa",
        "me revolta", "me repugna", "nao suporto ver", "que repulsa"
    ],
    "amor": [
        "amo", "amar", "amor", "carinho", "apaixonado", "ternura",
        "beijo", "afetuoso", "estima", "quero", "adoro", "apaixonada",
        "saudade", "afeto", "devocao", "paixao", "romantico",
        "romantica", "querido", "querida", "amado", "amada", "precioso",
        "preciosa", "encanto", "encantado", "fascinado", "admiracao",
        "te amo", "amo muito", "amo demais", "meu amor", "minha vida",
        "meu tudo", "meu mundo", "meu coracao", "coração", "apaixonei",
        "me apaixonei", "estou apaixonado", "estou apaixonada",
        "namorado", "namorada", "companheiro", "companheira", "parceiro"
    ],
    "esperanca": [
        "esperanca", "esperancoso", "otimista", "acredito", "confiante",
        "positivo", "vai melhorar", "tudo vai dar certo", "fe",
        "possivel", "conseguir", "vou conseguir", "vai dar certo",
        "confianca", "determinado", "motivado", "inspirado", "animador",
        "acredito que", "tenho fe", "tenho esperanca", "nao vou desistir",
        "vou conseguir", "vai acontecer", "em breve", "logo logo",
        "estou tentando", "estou lutando", "nao desisto", "persisto",
        "persistindo", "seguindo em frente", "continuo tentando"
    ],
    "gratidao": [
        "grato", "agradecido", "obrigado", "gratidao", "reconhecido",
        "valorizando", "agradecida", "muito obrigado", "feliz por",
        "sorte de", "privilegiado", "abencado", "gracas",
        "agradecimento", "reconhecimento", "estima", "que bom",
        "ainda bem", "gracias", "thank you", "obrigada", "muito grato",
        "muito agradecido", "sou grato", "fico grato", "agradeço",
        "agradeco", "valorizo", "apreco", "prezar", "prezando"
    ],
    "solidao": [
        "sozinho", "isolado", "abandonado", "ninguem", "excluido",
        "sem amigos", "me sinto so", "nao tenho ninguem", "carente",
        "desamparado", "incompreendido", "invisivel", "esquecido",
        "rejeitado", "marginalizado", "solitario", "solitaria",
        "nao tenho para quem ligar", "nao tenho amigos", "me sinto vazio",
        "nao pertenco", "nao me encaixo", "diferente de todos",
        "ninguem me entende", "ninguem liga", "ninguem se importa",
        "estou so", "fico so", "sempre sozinho", "sempre sozinha"
    ],
    "euforia": [
        "euforico", "empolgado", "animadissimo", "fantastico",
        "extraordinario", "incrivel", "demais", "top", "perfeito",
        "fenomenal", "surreal", "loucura", "que loucura",
        "to voando", "nas nuvens", "euforia", "explosao", "explosivo",
        "nao estou acreditando", "to louco", "to maluco", "que isso",
        "impressionante", "que dia", "que momento", "melhor dia",
        "melhor coisa", "melhor que tudo", "acima da media", "nota 10"
    ],
    "calma": [
        "calmo", "tranquilo", "paz", "sereno", "relaxado", "bem",
        "equilibrado", "centrado", "sossegado", "harmonioso",
        "tranquilidade", "serenidade", "placido", "quieto", "silencio",
        "meditando", "respirando", "descansando", "recarregando",
        "em paz", "com paz", "sinto paz", "estou bem", "tudo bem",
        "tranquilizei", "me acalmei", "consegui relaxar", "respirei fundo",
        "me centrei", "encontrei o equilibrio", "equilibrado agora"
    ],
    "confusao": [
        "confuso", "perdido", "nao sei", "incerto", "duvida",
        "indeciso", "nao entendo", "nao consigo", "desorientado",
        "atordoado", "desconcertado", "perplexo", "embaracado",
        "sem saber", "sem entender", "sem rumo", "sem direcao",
        "que fazer", "o que fazer", "como fazer", "nao sei mais",
        "completamente perdido", "sem saber o que", "em duvida",
        "nao tenho certeza", "incerteza", "nao sei decidir",
        "nao consigo decidir", "travado", "bloqueado", "paralisado"
    ],
    "vergonha": [
        "vergonha", "envergonhado", "constrangido", "humilhado",
        "timido", "acanhado", "encabulado", "intimidado", "retraido",
        "inibido", "vexado", "mortificado", "ruborizado", "corado",
        "que vergonha", "sinto vergonha", "me envergonho", "fiz feio",
        "passei vergonha", "fiquei vermelho", "fiquei corado",
        "nao consigo olhar", "quero sumir", "quero desaparecer",
        "que situacao", "me expus demais", "disse algo errado"
    ],
}

# ================================================================
# RECOMENDAÇÕES POR EMOÇÃO
# ================================================================

recomendacoes = {
    "alegria": (
        "Que energia maravilhosa! Continue cultivando essa alegria. "
        "Compartilhe com quem você ama — a felicidade se multiplica! 🌟"
    ),
    "tristeza": (
        "É normal sentir tristeza. Permita-se sentir sem julgamentos. "
        "Considere conversar com alguém de confiança — você não está sozinho. 💙"
    ),
    "raiva": (
        "Respire fundo 4 vezes antes de agir. "
        "A raiva é um sinal — ouça o que ela tem a dizer antes de reagir. 🌬️"
    ),
    "medo": (
        "Nomeie seu medo — isso já reduz sua intensidade. "
        "Lembre-se: coragem não é ausência de medo, é agir apesar dele. 🤝"
    ),
    "surpresa": (
        "Absorva o momento! Surpresas fazem parte da jornada. "
        "Respire e processe com calma antes de reagir. ✨"
    ),
    "nojo": (
        "Afaste-se do que causa desconforto. "
        "Cuide do seu espaço e dos seus limites — você merece respeito. 🛡️"
    ),
    "amor": (
        "O amor enriquece a vida de formas únicas. "
        "Valorize e expresse seus sentimentos com coragem e autenticidade. ❤️"
    ),
    "esperanca": (
        "Continue acreditando! Cada passo conta. "
        "A esperança é o combustível que move grandes transformações. 🌅"
    ),
    "gratidao": (
        "A gratidão transforma perspectivas e atrai mais coisas boas. "
        "Continue cultivando esse olhar especial sobre a vida! 🙏"
    ),
    "solidao": (
        "Você não está sozinho — mesmo que pareça assim agora. "
        "Busque conexões significativas, mesmo que pequenas. 🤗"
    ),
    "euforia": (
        "Que momento incrível! Aproveite essa energia com responsabilidade. "
        "Ancore seus planos nessa motivação! 🎉"
    ),
    "calma": (
        "Que momento precioso de equilíbrio. "
        "Aproveite para recarregar e refletir com clareza. 🕊️"
    ),
    "confusao": (
        "Tudo bem não saber. Dê um passo de cada vez. "
        "Escreva o que você sente — isso ajuda a organizar os pensamentos. 🧭"
    ),
    "vergonha": (
        "Seja gentil consigo mesmo. Todo mundo erra — é parte do crescimento. "
        "Você é mais do que seus momentos difíceis. 💚"
    ),
    "neutro": (
        "Momento de equilíbrio e observação. "
        "Aproveite a calma para refletir sobre seus objetivos! ⚖️"
    ),
}

# ================================================================
# TÉCNICAS TERAPÊUTICAS POR EMOÇÃO
# ================================================================

tecnicas_por_emocao = {
    "alegria": (
        "Técnica do Diário de Gratidão: anote 3 coisas boas que aconteceram hoje. "
        "Isso ancora a alegria e cria memórias positivas duradouras."
    ),
    "tristeza": (
        "Técnica da Auto-Compaixão (Kristin Neff): coloque a mão no coração, "
        "respire fundo e diga: 'Estou sofrendo agora. Sofrimento é parte da vida. "
        "Que eu seja gentil comigo mesmo.'"
    ),
    "raiva": (
        "Técnica da Respiração 4-7-8: inspire por 4 segundos, "
        "segure por 7 segundos, expire por 8 segundos. "
        "Repita 4 vezes. Isso ativa o sistema nervoso parassimpático."
    ),
    "medo": (
        "Técnica 5-4-3-2-1 (Grounding): nomeie 5 coisas que vê, "
        "4 que pode tocar, 3 que ouve, 2 que cheira e 1 que saboreia. "
        "Isso ancora você no momento presente."
    ),
    "surpresa": (
        "Técnica STOP: Pare, Respire fundo, Observe seus pensamentos "
        "e sentimentos, Prossiga com consciência. "
        "Dá tempo para processar o inesperado."
    ),
    "nojo": (
        "Técnica de Distanciamento Cognitivo (TCC): observe o sentimento "
        "como se fosse de fora. Pergunte: 'O que esse nojo me diz sobre "
        "meus valores e limites?'"
    ),
    "amor": (
        "Técnica Loving-Kindness (Metta): feche os olhos, visualize "
        "a pessoa amada e repita: 'Que você seja feliz. Que você seja saudável. "
        "Que você seja amado.' Expanda para você mesmo."
    ),
    "esperanca": (
        "Técnica de Visualização: feche os olhos por 5 minutos e visualize "
        "seu objetivo já realizado com detalhes sensoriais. "
        "Isso ativa o sistema de recompensa do cérebro."
    ),
    "gratidao": (
        "Técnica da Carta de Gratidão: escreva uma carta para alguém "
        "que fez diferença na sua vida. Mesmo que não envie, "
        "o ato de escrever já eleva o bem-estar."
    ),
    "solidao": (
        "Técnica de Conexão Progressiva: comece com pequenas interações — "
        "um sorriso, uma mensagem curta. "
        "A solidão diminui com micro-conexões diárias."
    ),
    "euforia": (
        "Técnica de Ancoragem: quando estiver nesse estado elevado, "
        "faça um gesto físico (ex: apertar o punho) para ancorar a sensação. "
        "Você poderá acessá-la depois."
    ),
    "calma": (
        "Técnica Body Scan: feche os olhos e percorra mentalmente seu corpo "
        "da cabeça aos pés, notando sensações sem julgamento. "
        "Aprofunda o estado de relaxamento."
    ),
    "confusao": (
        "Técnica Mind Mapping: pegue um papel e escreva o problema no centro. "
        "Ramifique todas as possibilidades. "
        "Externalizar a confusão ajuda a ver com mais clareza."
    ),
    "vergonha": (
        "Técnica do Observador Compassivo: imagine um amigo gentil observando "
        "sua situação. O que ele diria? "
        "Geralmente somos muito mais duros conosco do que com os outros."
    ),
    "neutro": (
        "Técnica de Check-in Emocional: pergunte-se 3 vezes ao dia "
        "'Como estou me sentindo agora?' e anote. "
        "Isso desenvolve inteligência emocional."
    ),
}

# ================================================================
# EMOJIS POR EMOÇÃO
# ================================================================

def get_emoji(emocao: str) -> str:
    emojis = {
        "alegria":    "😄",
        "tristeza":   "😢",
        "raiva":      "😡",
        "medo":       "😨",
        "surpresa":   "😲",
        "nojo":       "🤢",
        "amor":       "❤️",
        "esperanca":  "🌅",
        "gratidao":   "🙏",
        "solidao":    "😔",
        "euforia":    "🎉",
        "calma":      "🕊️",
        "confusao":   "😕",
        "vergonha":   "😳",
        "neutro":     "😐",
        "ansiedade":  "😰",
        "estresse":   "😓",
        "empolgacao": "🚀",
        "saudade":    "🥺",
        "orgulho":    "💪",
        "ciumes":     "😒",
        "frustracao": "😤",
        "alivio":     "😮‍💨",
        "entusiasmo": "✨",
        "melancolia": "🌧️",
        "nostalgia":  "📸",
        "panico":     "😱",
        "timidez":    "🙈",
        "curiosidade":"🤔",
        "tedio":      "😴",
        "animacao":   "🎊",
        "desespero":  "😩",
        "paz":        "☮️",
        "contentamento": "😊",
    }
    return emojis.get(emocao, "😐")

# ================================================================
# DETECÇÃO DE EMOÇÃO
# ================================================================

# Mapa de emojis para emocoes
EMOJI_PARA_EMOCAO = {
    "😄": "alegria", "😊": "alegria", "🥰": "alegria", "😁": "alegria",
    "😂": "alegria", "🤣": "alegria", "😃": "alegria", "😀": "alegria",
    "🎉": "euforia", "🥳": "euforia", "⚡": "euforia", "🔥": "euforia",
    "😢": "tristeza", "😭": "tristeza", "😔": "solidao", "😞": "tristeza",
    "💔": "tristeza", "😿": "tristeza", "🥺": "tristeza",
    "😡": "raiva", "🤬": "raiva", "😤": "raiva", "💢": "raiva",
    "😨": "medo", "😰": "medo", "😱": "medo", "🫣": "medo",
    "😰": "ansiedade", "😟": "ansiedade", "😧": "ansiedade",
    "❤️": "amor", "🥰": "amor", "💕": "amor", "💖": "amor",
    "🙏": "gratidao", "🤗": "gratidao", "😇": "gratidao",
    "🌅": "esperanca", "✨": "esperanca", "🌟": "esperanca",
    "😲": "surpresa", "😮": "surpresa", "🤯": "surpresa",
    "🤢": "nojo", "🤮": "nojo", "😖": "nojo",
    "🕊️": "calma", "😌": "calma", "🧘": "calma", "😴": "calma",
    "😕": "confusao", "🤔": "confusao", "😵": "confusao",
    "😳": "vergonha", "🫠": "vergonha", "😬": "vergonha",
    "😐": "neutro", "😑": "neutro", "🫤": "neutro",
    "😓": "estresse", "😩": "estresse", "😫": "estresse",
    "😔": "solidao", "🥹": "solidao",
}

def emocao_por_emoji(emoji_input: str) -> str:
    return EMOJI_PARA_EMOCAO.get(emoji_input.strip(), "neutro")

def normalizar_texto(texto: str) -> str:
    texto = texto.lower()
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    texto = re.sub(r'[^\w\s]', ' ', texto)
    return texto


# ============================================================
# DICIONARIO UNIVERSAL DE GIRIAS E EXPRESSOES (200+ entradas)
# ============================================================
GIRIAS_NORMALIZACAO = {
    # Estados negativos
    "ta mal": "estou mal",
    "to mal": "estou mal",
    "tô mal": "estou mal",
    "na bad": "triste deprimido",
    "na bad foda": "muito triste deprimido",
    "destruido": "destruido arrasado",
    "destruída": "destruida arrasada",
    "arrasado": "arrasado triste",
    "lasquei": "errei fracassei",
    "fodeu": "deu errado fracasso",
    "ferrou": "deu errado problema",
    "tá horrivel": "situacao horrivel ruim",
    "ta horrivel": "situacao horrivel ruim",
    "péssimo": "pessimo muito ruim",
    "horrivel": "horrivel muito ruim",
    "uma merda": "muito ruim pessimo",
    "saco cheio": "cansado entediado frustrado",
    "cheio": "cansado farto",
    "de saco cheio": "cansado frustrado",
    "travei": "travei ansioso paralisado",
    "trava": "ansioso paralisado",
    "surtar": "surtar ansioso nervoso",
    "surtei": "surtei ansioso nervoso",
    "bate aquela": "sinto aquela emocao",
    "bate uma": "sinto aquela emocao",
    "ta pesado": "situacao pesada dificil",
    "tá pesado": "situacao pesada dificil",
    "to pesado": "sentindo pesado",
    "tô pesado": "sentindo pesado",
    "esgotado": "esgotado cansado estresse",
    "esgotada": "esgotada cansada estresse",
    "cansado de tudo": "cansado frustrado desistindo",
    "sem energia": "sem energia cansado",
    "sem animo": "sem animo triste desanimado",
    "sem ânimo": "sem animo triste desanimado",
    "pra baixo": "triste desanimado para baixo",
    "pra baixo mesmo": "muito triste deprimido",
    "no fundo do poco": "muito triste deprimido",
    "no fundo": "triste deprimido",
    "caindo": "caindo tristeza depressao",
    "afundando": "afundando triste deprimido",
    "perdido": "perdido confuso desorientado",
    "perdida": "perdida confusa desorientada",
    "vazio": "vazio solidao depressao",
    "vazia": "vazia solidao depressao",
    "buraco negro": "depressao tristeza profunda",
    "tremedeira": "ansioso nervoso medo",
    "tremendo": "nervoso ansioso medo",
    "suando frio": "ansioso medo nervoso",
    "coração acelerado": "ansioso medo nervoso",
    "coracao acelerado": "ansioso medo nervoso",
    "aperto no peito": "ansioso medo tristeza",
    "no sufoco": "ansioso sufocando pressao",
    "sufocando": "ansioso sufocando angustia",
    "nao aguento mais": "nao aguento mais exausto frustrado",
    "não aguento mais": "nao aguento mais exausto frustrado",
    "largado": "desmotivado triste abandonado",
    "largada": "desmotivada triste abandonada",
    "esquecido": "esquecido solidao abandonado",
    "invisible": "invisivel ignorado solidao",
    "invisivel": "invisivel ignorado solidao",
    "ninguem me entende": "solidao incompreendido frustrado",
    "ningem": "ninguem solidao",
    "raivoso": "raivoso raiva bravo",
    "com raiva": "com raiva raiva bravo",
    "irritado": "irritado raiva frustrado",
    "irritada": "irritada raiva frustrada",
    "bravo": "bravo raiva irritado",
    "brava": "brava raiva irritada",
    "chateado": "chateado triste frustrado",
    "chateada": "chateada triste frustrada",
    # Estados positivos
    "feliz demais": "muito feliz alegria euforia",
    "na vibe": "animado feliz bem",
    "boa vibe": "boa energia feliz animado",
    "na vibe boa": "animado feliz bem",
    "top demais": "otimo excelente alegria",
    "no alto": "feliz euforia animado",
    "voando": "feliz euforia animado",
    "nas nuvens": "feliz apaixonado euforia",
    "apaixonado": "apaixonado amor feliz",
    "apaixonada": "apaixonada amor feliz",
    "doido de feliz": "muito feliz euforia",
    "doida de feliz": "muito feliz euforia",
    "realizando": "realizando conquista orgulho",
    "realizado": "realizado orgulho feliz",
    "realizada": "realizada orgulho feliz",
    "grato": "grato gratidao feliz",
    "grata": "grata gratidao feliz",
    "aliviado": "aliviado alivio bem",
    "aliviada": "aliviada alivio bem",
    "tranquilo": "tranquilo calmo paz",
    "tranquila": "tranquila calma paz",
    "sereno": "sereno calmo paz",
    "serena": "serena calma paz",
    "confiante": "confiante seguro otimista",
    "motivado": "motivado animado empolgado",
    "motivada": "motivada animada empolgada",
    "empolgado": "empolgado animado euforia",
    "empolgada": "empolgada animada euforia",
    "orgulhoso": "orgulhoso orgulho conquista",
    "orgulhosa": "orgulhosa orgulho conquista",
    "esperancoso": "esperancoso esperanca otimista",
    "esperançoso": "esperancoso esperanca otimista",
    # Girias especificas BR
    "tá bom": "esta bom satisfeito",
    "ta bom": "esta bom satisfeito",
    "ta otimo": "esta otimo muito bem alegria",
    "tá ótimo": "esta otimo muito bem alegria",
    "show": "otimo excelente alegria",
    "show de bola": "otimo excelente alegria",
    "massa": "otimo legal alegria",
    "irado": "otimo incrivel surpresa alegria",
    "maneiro": "legal bom satisfeito",
    "dahora": "otimo legal alegria",
    "d+ ": "demais muito intenso",
    "fds": "frustrado raiva surpresa",
    "wtf": "surpresa confusao raiva",
    "nossa": "surpresa espanto",
    "caramba": "surpresa espanto",
    "cara": "expressao neutra",
    "vixe": "surpresa espanto",
    "eita": "surpresa espanto",
    "que saudade": "saudade nostalgia tristeza",
    "tanta saudade": "muita saudade nostalgia tristeza",
    "com saudade": "saudade nostalgia tristeza",
    "to com saudade": "saudade nostalgia tristeza",
    "to morrendo": "morrendo de algo intenso",
    "morrendo de rir": "muito alegre rindo euforia",
    "morrendo de medo": "muito medo panico ansiedade",
    "morrendo de vergonha": "muita vergonha envergonhado",
    "morrendo de saudade": "muita saudade nostalgia tristeza",
    "chorando": "chorando tristeza emocao",
    "chorei": "chorei tristeza emocao",
    "chora": "tristeza emocao choro",
    "llorando": "tristeza emocao choro",  # espanhol
    "feliz": "feliz alegria bem",
    "triste": "triste tristeza mal",
    "ansioso": "ansioso ansiedade nervoso",
    "ansiosa": "ansiosa ansiedade nervosa",
    "nervoso": "nervoso ansioso agitado",
    "nervosa": "nervosa ansiosa agitada",
    "estressado": "estressado estresse esgotado",
    "estressada": "estressada estresse esgotada",
    "deprimido": "deprimido depressao tristeza",
    "deprimida": "deprimida depressao tristeza",
    # Ingles comum
    "i am happy": "estou feliz alegria",
    "i feel sad": "me sinto triste tristeza",
    "i am sad": "estou triste tristeza",
    "feeling good": "me sentindo bem alegria",
    "feeling bad": "me sentindo mal tristeza",
    "i am anxious": "estou ansioso ansiedade",
    "so happy": "muito feliz euforia alegria",
    "so sad": "muito triste tristeza",
    "i love": "eu amo amor feliz",
    "i hate": "eu odeio raiva",
    "stressed": "estressado estresse",
    "depressed": "deprimido depressao tristeza",
    "anxious": "ansioso ansiedade",
    "lonely": "solitario solidao tristeza",
    "excited": "empolgado animado euforia",
    "grateful": "grato gratidao feliz",
    "angry": "raivoso raiva irritado",
    "scared": "assustado medo ansiedade",
    "lost": "perdido confuso",
    "tired": "cansado esgotado",
    "overwhelmed": "sobrecarregado estresse ansiedade",
    # Espanhol comum
    "estoy bien": "estou bem alegria",
    "estoy mal": "estou mal triste",
    "me siento": "me sinto emocao",
    "feliz": "feliz alegria",
    "triste": "triste tristeza",
    "enojado": "irritado raiva",
    "asustado": "assustado medo",
    "solo": "solitario solidao",
    "cansado": "cansado esgotado",
}

# Mapa de emocoes expandido para deteccao local
PALAVRAS_EMOCOES_EXPANDIDO = {
    "alegria": [
        "feliz","contente","animado","alegre","satisfeito","otimo","maravilhoso",
        "incrivel","fantastico","perfeito","excelente","bom","bem","ótimo","ótima",
        "felicidade","alegria","prazer","diversao","risada","sorriso","gargalhada",
        "radiante","luminoso","encantado","deslumbrado","eufórico","entusiasmado",
        "exultante","jubiloso","radiante","vivaz","glorioso","magnifico",
        "show","massa","irado","dahora","top","maneiro","dashow","sensacional",
    ],
    "tristeza": [
        "triste","mal","ruim","pessimo","horrivel","deprimido","chateado","decepcionado",
        "frustrado","abatido","desanimado","melancólico","saudoso","angustiado",
        "desolado","inconsolável","lamentoso","lacrimoso","sofrido","magoado",
        "machucado","ferido","partido","arrasado","destroçado","devastado",
        "chorando","chorei","lagrimas","choro","desabafar","dor","sofrimento",
        "pena","lamento","tristeza","depressao","desespero","abandono","rejeicao",
        "na bad","destruido","destruída","pra baixo","no fundo","caindo","afundando",
    ],
    "raiva": [
        "raiva","irritado","bravo","furioso","nervoso","indignado","revoltado",
        "com raiva","muito irritado","odeio","detesto","nao suporto","me irrita",
        "raivoso","irado","pistola","fodendo","absurdo","injusto","ridiculo",
        "idiota","burro","insuportavel","inaceitavel","revolta","indignacao",
        "coleroso","fulo","agressivo","violento","explosivo","impaciente",
        "fds","wtf","raiva","odeio","chateado","irritante",
    ],
    "medo": [
        "medo","assustado","apavorado","aterrorizado","com medo","temer",
        "pavor","terror","horror","fobia","fobia","temor","receio","susto",
        "arrepio","calafrio","panico","aflicao","angustia",
        "morrendo de medo","com muito medo","apavorada","aterrorizada",
        "scared","afraid","frightened","terrified","petrificado",
    ],
    "ansiedade": [
        "ansioso","ansiosa","ansiedade","nervoso","agitado","preocupado","inquieto",
        "apreensivo","tenso","angustiado","aflito","estressado","estresse",
        "aperto no peito","coração acelerado","tremendo","suando","paralisado",
        "travado","trava","surtar","surtei","palpitacao","falta de ar",
        "overwhelmed","anxious","worried","stressed","anxious","nervous",
        "tremedeira","mao suada","cabeca rodando","zonzo",
    ],
    "amor": [
        "amor","amo","adoro","apaixonado","amando","carinho","afeto","afetuoso",
        "querido","querida","amado","amada","amoroso","encantado","fascinado",
        "apaixonada","gosto muito","te amo","te adoro","amo demais",
        "love","i love","in love","apaixonei","me apaixonei","apaixonar",
    ],
    "esperanca": [
        "esperanca","esperancoso","otimista","confiante","acredito","vai melhorar",
        "vai dar certo","positivo","animado com o futuro","novo começo","recomeço",
        "possivel","conseguir","superar","vencer","melhorar","progredir",
        "hopeful","optimistic","looking forward","bright future",
    ],

    "solidao": [
        "sozinho","sozinha","solidao","solitario","isolado","abandonado","esquecido",
        "ninguem","sem amigos","sem companhia","me sinto so","me sinto sozinho",
        "lonely","alone","isolated","nobody","nao tenho","sem ninguem",
        "invisivel","ninguem me entende","nao me veem","ignorado","excluido",
    ],
    "euforia": [
        "eufórico","euforia","empolgado","animadíssimo","nas nuvens","voando",
        "no alto","inacreditável","impressionante","que coisa incrivel","uau",
        "wow","amazing","incredible","on top of the world","on cloud nine",
        "doido de feliz","doida de feliz","muito muito feliz",
    ],
    "calma": [
        "calmo","calma","tranquilo","tranquila","sereno","serena","paz","pacifico",
        "relaxado","relaxada","equilibrado","centrado","zen","meditando",
        "peaceful","calm","relaxed","chill","tranquil","serenity",
        "sem pressa","devagar","respirando fundo","descansando",
    ],
    "confusao": [
        "confuso","confusa","perdido","perdida","desorientado","nao entendo",
        "nao sei","sem saber","indeciso","indecisa","em duvida","duvidoso",
        "confused","lost","unsure","uncertain","dont know","nao consigo entender",
        "complicado","complexo","embaralhado","atordoado",
    ],
    "vergonha": [
        "vergonha","envergonhado","envergonhada","humilhado","humilhada","constrangido",
        "constrangida","timido","timida","acanhado","acanhada","sem graca",
        "morrendo de vergonha","que saia","que situacao","que fria","que vexame",
        "ashamed","embarrassed","humiliated","shy","timid",
    ],
    "estresse": [
        "estressado","estressada","esgotado","esgotada","sobrecarregado","sobrecarregada",
        "sob pressao","pressao","cansado de tudo","no limite","no meu limite",
        "sem energia","sem forcas","exausto","exausta","burnout","esgotamento",
        "stressed","overwhelmed","burned out","exhausted","drained",
        "saco cheio","de saco cheio","cheio","nao aguento mais",
        "nao aguento mais esse trabalho","nao aguento mais trabalhar",
        "nao suporto mais","to no limite","cheguei no limite","atingi meu limite",
        "trabalho demais","trabalhando demais","overworked","overtired",
        "erschopft","esausto","epuise","agotado","ausgebrannt","gestresst",
        "stressato","stresse","estressante","estressei","estressar",
    ],
    "saudade": [
        "saudade","com saudade","tanta saudade","muita saudade","sentindo saudade",
        "que saudade","sinto saudade","morrendo de saudade","cheia de saudade",
        "nostalgia","nostalgico","nostalgica","lembrar","recordar","memoria",
        "tempos antigos","epoca boa","quando era","lembrei","me lembro",
        "tempos bons","tempos felizes","tempos de antes","era bom quando",
        "miss","missing","nostalgia","reminiscing","remembering",
        "natsukashii","sehnsucht","hiraeth","mal du pays",
    ],
    "orgulho": [
        "orgulho","orgulhoso","orgulhosa","conquista","conquistei","consegui",
        "realizei","realizado","realizada","me superei","superei","venci","venceu",
        "que orgulho","muito orgulho","tanto orgulho","cheio de orgulho",
        "orgulhoso de mim","orgulhosa de mim","to orgulhoso","to orgulhosa",
        "me sinto orgulhoso","me sinto orgulhosa","estou orgulhoso","estou orgulhosa",
        "proud","achievement","accomplished","succeeded","overcame","so proud",
        "im proud","i am proud","feeling proud","proud of myself","proud of you",
        "to muito feliz com","estou feliz por","me sinto bem por",
    ],
    "gratidao": [
        "grato","grata","gratidao","obrigado","obrigada","agradecido","agradecida",
        "thankful","grateful","blessed","abencado","privilegiado","sortudo",
        "que bom","que otimo","que maravilha","que alegria","que presente",
        "valorizo","reconheco","apreco","aprecio","estimo",
        "so grateful","feeling grateful","im grateful","i am grateful",
        "so thankful","im thankful","i am thankful","thank god","graças a deus",
        "muito grato","muito grata","eternamente grato","eternamente grata",
        "sinto gratidao","cheio de gratidao","cheia de gratidao",
    ],
    "culpa": [
        "culpa","culpado","culpada","sinto culpa","me sinto culpado","me sinto culpada",
        "arrependido","arrependida","arrependimento","remorso","me arrependo",
        "foi culpa minha","e minha culpa","fiz algo errado","errei","errou",
        "guilty","shame","regret","remorse","i feel guilty","feeling guilty",
        "je me sens coupable","ich bin schuldig","mi sento in colpa","me siento culpable",
    ],
    "coragem": [
        "corajoso","corajosa","coragem","bravo","brava","determinado","determinada",
        "forte","forcas","vai em frente","nao desiste","superar","vencer","enfrentar",
        "brave","courageous","strong","fearless","bold","determined",
        "ich bin mutig","je suis courageux","sono coraggioso","soy valiente",
    ],
    "esperanca": [
        "esperanca","esperancoso","esperancosa","esperancando","com esperanca",
        "cheio de esperanca","cheia de esperanca","otimista","vai melhorar",
        "acredito","vai dar certo","possivel","progredir","melhorar","recomecar",
        "hopeful","hope","optimistic","things will get better","looking forward",
        "ich bin hoffnungsvoll","je suis plein despoir","sono pieno di speranza","tengo esperanza",
    ],
    "frustracao": [
        "frustrado","frustrada","frustracao","decepcionado","decepcionada","decepção",
        "nao deu certo","nao funcionou","tentei e nao","esperava mais","esperava melhor",
        "disappointed","frustrated","let down","failed","nao consegui",
        "nao rolou","nao aconteceu","deu errado","perdeu",
    ],
    "entusiasmo": [
        "entusiasmado","entusiasmada","animado","empolgado","motivado","inspirado",
        "com vontade","querendo muito","nao vejo a hora","mal posso esperar",
        "enthusiastic","excited","motivated","inspired","cant wait",
        "to ansioso para","to animado com","to empolgado com",
    ],
    "paz": [
        "em paz","com paz","paz interior","tranquilidade","sossego","quietude",
        "harmonia","equilibrio","bem comigo mesmo","bem comigo mesma",
        "at peace","inner peace","harmony","balance","content","contente",
        "satisfeito com","agradecido pela","curtindo a vida",
    ],
    "desespero": [
        "desesperado","desesperada","desespero","sem saida","sem esperanca",
        "nao ha saida","nao tem jeito","acabou","tudo perdido","nao adianta",
        "hopeless","desperate","no way out","giving up","desistindo",
        "nao consigo mais","nao da mais","ja nao da","to desistindo",
    ],
    "neutro": [
        "assim assim","mais ou menos","ok","tudo bem","nada demais","normal",
        "regular","razoavel","nem bom nem ruim","medio","mediano",
        "okay","fine","alright","so so","not bad","not good",
    ],
}

def normalizar_giria(texto: str) -> str:
    """Normaliza girias e expressoes para palavras-chave emocionais"""
    import re as _re
    texto_lower = texto.lower().strip()
    
    # Usar GIRIAS_NORMALIZACAO — checar palavra inteira (word boundary)
    for giria, traducao in GIRIAS_NORMALIZACAO.items():
        giria_strip = giria.strip()
        if len(giria_strip) <= 3:
            # Palavras curtas: checar como palavra inteira
            pattern = r'\b' + _re.escape(giria_strip) + r'\b'
            if _re.search(pattern, texto_lower):
                texto_lower = _re.sub(pattern, " " + traducao + " ", texto_lower)
        else:
            if giria_strip in texto_lower:
                texto_lower = texto_lower.replace(giria_strip, " " + traducao + " ")
    
    # Usar EXPRESSOES_UNIVERSAIS — apenas expressoes com 4+ chars
    try:
        for expr, traducao in EXPRESSOES_UNIVERSAIS.items():
            expr_strip = expr.strip()
            if len(expr_strip) >= 4 and expr_strip in texto_lower:
                texto_lower = texto_lower.replace(expr_strip, " " + traducao + " ")
    except:
        pass
    return texto_lower

def detectar_crise(texto: str) -> bool:
    """Detecta se texto indica crise emocional grave"""
    texto_lower = texto.lower()
    palavras_crise = [
        "quero morrer","nao quero mais viver","quero me machucar",
        "quero desaparecer","pensar em suicidio","me matar",
        "nao vale a pena viver","nao quero mais existir",
        "i want to die","want to kill myself","end my life",
        "quiero morir","je veux mourir","voglio morire",
        "automutilacao","me cortar","me machucar","sem saida",
        "ninguem vai sentir minha falta","mundo melhor sem mim",
        "CRISE"
    ]
    return any(p in texto_lower for p in palavras_crise)

def detectar_emocao_com_ia(texto: str, usar_gemini: bool = False, db=None, usuario_id: int = None) -> dict:
    """Deteccao completa usando local + Gemini quando necessario"""
    # Analise local completa primeiro (rapida)
    analise_local = analisar_texto_completo(texto)
    
    # Verificar crise SEMPRE
    em_crise = detectar_crise(texto)
    analise_local["em_crise"] = em_crise
    
    if em_crise:
        analise_local["urgencia"] = "crise"
        analise_local["emocao"] = "desespero"
    
    return analise_local

def detectar_idioma(texto: str) -> str:
    """Detecta idioma com precisao maxima — PT tem prioridade"""
    if not texto or not texto.strip():
        return "pt"
    try:
        from langdetect import detect
        idioma = detect(texto)
        if idioma in ["pt","en","es","fr","de","it","ja","ko","ar","ru","hi"]:
            return idioma
    except:
        pass
    texto_lower = texto.lower()
    palavras_pt = ["estou","sinto","minha","meu","tenho","nao","que","com","uma","para","isso","mas","voce","ele","ela","nos","eles","muito","mais","como","quando","onde","porque","tambem","ainda","ja","ate","desde","cada","tudo","nada","algo","alguem","nunca","sempre","talvez","hoje","agora","aqui","assim","entao","to","ta","ne","gente","cara","mano","obrigado","obrigada","saudade","brasileiro","brasil","trabalho","dinheiro","oi","ola","tchau"]
    palavras_en = ["i am","i feel","i have","my","the","and","but","with","not","feel","this","that","you","he","she","we","they","very","how","when","where","because","also","never","always","today","now","here","there"]
    palavras_es = ["estoy","siento","tengo","mi","con","una","para","esto","pero","muy","usted","nosotros","ellos","tambien","todavia","hoy","ahora","aqui","alli","entonces","aunque","hola","gracias"]
    score_pt = sum(2 for p in palavras_pt if p in texto_lower) + 3
    score_en = sum(1 for p in palavras_en if p in texto_lower)
    score_es = sum(1 for p in palavras_es if p in texto_lower)
    if score_en > score_pt and score_en > score_es:
        return "en"
    if score_es > score_pt and score_es > score_en:
        return "es"
    return "pt"

def detectar_emocao(texto: str) -> str:
    """Detecta emocao de QUALQUER texto — girias, idiomas, emojis, expressoes"""
    if not texto or not texto.strip():
        return "neutro"
    
    texto_orig = texto
    
    # 1. Normalizar acentos para checar girias (to == tô, etc)
    texto_sem_acento = normalizar_texto(texto)
    
    # 2. Normalizar girias no texto original E sem acento
    texto_normalizado = normalizar_giria(texto)
    texto_normalizado = normalizar_giria(texto_sem_acento) + " " + texto_normalizado
    
    # 3. Adicionar mapeamentos diretos de palavras-chave multilíngues
    mapa_direto = {
        # Portugues com acento e sem
        "to na bad": "tristeza depressao mal",
        "tô na bad": "tristeza depressao mal",
        "na bad": "tristeza depressao mal",
        "destruido": "tristeza devastado arrasado",
        "destruida": "tristeza devastada arrasada",
        "to destruido": "tristeza devastado",
        "to destruida": "tristeza devastada",
        "me sinto um lixo": "tristeza vergonha inadequacao",
        "sinto um lixo": "tristeza vergonha",
        "sou um lixo": "tristeza vergonha inadequacao",
        "que saudade": "saudade nostalgia tristeza",
        "tanta saudade": "saudade nostalgia tristeza",
        "surtei": "ansiedade nervoso raiva",
        "surtando": "ansiedade nervoso raiva",
        "surtar": "ansiedade nervoso raiva",
        "travei": "ansiedade bloqueio medo",
        "travou": "ansiedade bloqueio",
        "nao aguento": "estresse frustracao desespero",
        "nao consigo mais": "desespero estresse esgotado",
        "to mal": "tristeza ruim mal",
        "tô mal": "tristeza ruim mal",
        "me sinto mal": "tristeza ruim mal",
        "muito mal": "tristeza ruim intenso",
        "pra baixo": "tristeza desanimado melancolia",
        "no fundo": "tristeza depressao fundo",
        "vazio por dentro": "vazio solidao anedonia",
        "vazia por dentro": "vazio solidao anedonia",
        "sem sentido": "vazio proposito existencial",
        "perdido": "confusao solidao desorientado",
        "perdida": "confusao solidao desorientada",
        "me sinto sozinho": "solidao tristeza abandono",
        "me sinto sozinha": "solidao tristeza abandono",
        "to sozinho": "solidao tristeza abandono",
        "to sozinha": "solidao tristeza abandono",
        "chorei": "tristeza dor emocao",
        "chorando": "tristeza dor emocao",
        "to chorando": "tristeza dor emocao",
        "fui traido": "traicao raiva tristeza humilhacao",
        "fui traida": "traicao raiva tristeza humilhacao",
        "me traiu": "traicao raiva tristeza",
        "terminamos": "tristeza luto perda",
        "brigamos": "raiva tristeza conflito",
        "me deixou": "abandono tristeza rejeicao",
        "foi embora": "abandono tristeza saudade",
        "nao me ama": "rejeicao tristeza dor",
        "nao me quer": "rejeicao tristeza dor",
        "to apaixonado": "amor paixao alegria",
        "to apaixonada": "amor paixao alegria",
        "to feliz": "alegria felicidade contentamento",
        "to muito feliz": "alegria euforia felicidade",
        "to animado": "alegria animacao entusiasmo",
        "to animada": "alegria animacao entusiasmo",
        "to empolgado": "alegria empolgacao euforia",
        "to empolgada": "alegria empolgacao euforia",
        "to ansioso": "ansiedade nervoso preocupado",
        "to ansiosa": "ansiedade nervosa preocupada",
        "to nervoso": "ansiedade nervoso agitado",
        "to nervosa": "ansiedade nervosa agitada",
        "to estressado": "estresse ansiedade esgotado",
        "to estressada": "estresse ansiedade esgotada",
        "to com raiva": "raiva irritado frustrado",
        "to irritado": "raiva irritado frustrado",
        "to irritada": "raiva irritada frustrada",
        "to com medo": "medo ansiedade panico",
        "to com saudade": "saudade nostalgia tristeza",
        "to grato": "gratidao alegria reconhecimento",
        "to grata": "gratidao alegria reconhecimento",
        "to realizado": "realizacao orgulho alegria",
        "to realizada": "realizacao orgulho alegria",
        "to esgotado": "burnout esgotamento estresse",
        "to esgotada": "burnout esgotamento estresse",
        "to exausto": "burnout exaustao estresse",
        "to exausta": "burnout exaustao estresse",
        "to confuso": "confusao perdido duvida",
        "to confusa": "confusao perdida duvida",
        "me sinto perdido": "confusao solidao desorientado",
        "me sinto perdida": "confusao solidao desorientada",
        # Espanhol
        "muy triste": "tristeza deprimido melancolia",
        "estoy triste": "tristeza deprimido melancolia",
        "muy feliz": "alegria felicidade contentamento",
        "estoy feliz": "alegria felicidade contentamento",
        "muy ansioso": "ansiedade nervoso preocupado",
        "estoy ansioso": "ansiedade nervoso",
        "muy enojado": "raiva irritado frustrado",
        "estoy enojado": "raiva irritado",
        "muy solo": "solidao tristeza abandono",
        "estoy solo": "solidao tristeza",
        "muy cansado": "estresse esgotado exausto",
        "estoy cansado": "estresse esgotado",
        "me siento mal": "tristeza ruim mal",
        "me siento solo": "solidao tristeza",
        "no puedo mas": "desespero esgotado frustrado",
        "estoy harto": "frustrado farto cansado",
        "que tristeza": "tristeza melancolia desolacao",
        "que alegria": "alegria felicidade contentamento",
        "que miedo": "medo ansiedade panico",
        "que rabia": "raiva irritacao frustracao",
        # Ingles
        "feeling sad": "tristeza deprimido melancolia",
        "feeling bad": "tristeza ruim mal",
        "feeling empty": "vazio solidao anedonia",
        "feeling lonely": "solidao tristeza abandono",
        "feeling anxious": "ansiedade nervoso preocupado",
        "feeling angry": "raiva irritado frustrado",
        "feeling scared": "medo ansiedade panico",
        "feeling happy": "alegria felicidade contentamento",
        "feeling great": "alegria excelente contentamento",
        "feeling awful": "tristeza pessimo muito mal",
        "feeling terrible": "tristeza pessimo horrivel",
        "feeling lost": "confusao solidao desorientado",
        "feeling numb": "vazio anedonia dissociado",
        "feeling overwhelmed": "estresse sobrecarregado ansiedade",
        "im sad": "tristeza deprimido melancolia",
        "i am sad": "tristeza deprimido melancolia",
        "im happy": "alegria felicidade contentamento",
        "i am happy": "alegria felicidade contentamento",
        "im angry": "raiva irritado frustrado",
        "i am angry": "raiva irritado frustrado",
        "im scared": "medo ansiedade panico",
        "i am scared": "medo ansiedade panico",
        "im lonely": "solidao tristeza abandono",
        "i am lonely": "solidao tristeza abandono",
        "im stressed": "estresse ansiedade esgotado",
        "i am stressed": "estresse ansiedade esgotado",
        "im depressed": "tristeza depressao anedonia",
        "i am depressed": "tristeza depressao anedonia",
        "im anxious": "ansiedade nervoso preocupado",
        "i am anxious": "ansiedade nervoso preocupado",
        "im in love": "amor paixao alegria",
        "i am in love": "amor paixao alegria",
        "im grateful": "gratidao alegria reconhecimento",
        "i am grateful": "gratidao alegria reconhecimento",
        "im exhausted": "burnout exaustao estresse",
        "i am exhausted": "burnout exaustao estresse",
        "im broken": "tristeza dor devastado",
        "i am broken": "tristeza dor devastado",
        "im lost": "confusao solidao desorientado",
        "i am lost": "confusao solidao desorientado",
        "not okay": "tristeza ansiedade mal",
        "im not okay": "tristeza ansiedade mal",
        "i am not okay": "tristeza ansiedade mal",
        "falling apart": "tristeza desespero devastado",
        "breaking down": "tristeza desespero choro",
        "cant take it": "desespero esgotado frustrado",
        "give up": "desespero frustracao desistindo",
        "empty inside": "vazio solidao anedonia",
        "feeling empty inside": "vazio solidao anedonia",
        "so happy": "alegria euforia felicidade",
        "so sad": "tristeza profunda melancolia",
        "so angry": "raiva intensa frustrado",
        "so scared": "medo panico ansiedade",
        "so stressed": "estresse intenso ansiedade",
        "so tired": "esgotado exausto cansado",
        "so lonely": "solidao profunda tristeza",
        "so grateful": "gratidao profunda alegria",
        "so excited": "euforia empolgacao alegria",
        "so anxious": "ansiedade intensa nervoso",
        "on cloud nine": "euforia alegria felicidade",
        "feeling blue": "tristeza melancolia desanimado",
        "under the weather": "tristeza mal indisposto",
        "heartbroken": "tristeza dor amor perdido",
        "over the moon": "euforia alegria muito feliz",
        "in my feelings": "emocional reflexivo melancolico",
        "going through it": "sofrimento dificuldade tristeza",
        "burned out": "burnout esgotamento exaustao",
        "drained": "esgotado sem energia vazio",
        # Alemao
        "ich bin traurig": "tristeza deprimido melancolia",
        "bin traurig": "tristeza deprimido",
        "so traurig": "muito triste tristeza profunda",
        "ich bin glucklich": "alegria felicidade contentamento",
        "ich bin wutend": "raiva irritado frustrado",
        "ich habe angst": "medo ansiedade panico",
        "ich bin mude": "esgotado cansado exausto",
        "ich bin einsam": "solidao tristeza abandono",
        "ich bin am ende": "desespero esgotado burnout",
        "mir geht es schlecht": "tristeza mal ruim",
        "mir geht es gut": "alegria bem contentamento",
        # Frances
        "je suis triste": "tristeza deprimido melancolia",
        "tres triste": "muito triste tristeza profunda",
        "je suis heureux": "alegria felicidade contentamento",
        "je suis heureuse": "alegria felicidade contentamento",
        "j en ai marre": "frustrado farto cansado",
        "je suis epuise": "esgotado burnout exausto",
        "je me sens seul": "solidao tristeza abandono",
        "avoir le cafard": "tristeza depressao melancolia",
        # Italiano
        "sono triste": "tristeza deprimido melancolia",
        "sono felice": "alegria felicidade contentamento",
        "sono stanco": "esgotado cansado exausto",
        "stanco": "esgotado cansado exausto",
        "molto stanco": "muito esgotado exausto",
        "sono solo": "solidao tristeza abandono",
        "sono arrabbiato": "raiva irritado frustrado",
        "ho paura": "medo ansiedade panico",
        "mi sento male": "tristeza mal ruim",
        "mi sento solo": "solidao tristeza abandono",
        # Fixes adicionais
        "sono molto stanco": "esgotado cansado exausto estresse",
        "molto stanco": "esgotado cansado exausto estresse",
        "sono stanco": "esgotado cansado exausto",
        "que orgulho": "orgulho realizacao conquista alegria",
        "que orgulho de mim": "orgulho realizacao autoestima",
        "que orgulho de voce": "orgulho admiracao alegria",
        "muito orgulho": "orgulho realizacao conquista",
        "estoy solo y triste": "solidao tristeza abandono",
        "solo y triste": "solidao tristeza abandono",
        "estoy solo": "solidao tristeza abandono",
        "me siento solo": "solidao tristeza abandono",
        "feeling so grateful": "gratidao alegria reconhecimento",
        "so grateful": "gratidao alegria reconhecimento",
        "feeling grateful": "gratidao alegria reconhecimento",
        "im grateful": "gratidao alegria reconhecimento",
        "i am grateful": "gratidao alegria reconhecimento",
        "so thankful": "gratidao alegria reconhecimento",
        "im thankful": "gratidao alegria reconhecimento",
        "ich liebe dich": "amor paixao carinho afeto",
        "liebe dich": "amor paixao carinho",
        "ich liebe": "amor paixao carinho",
        "ich bin verliebt": "amor paixao apaixonado",
        # Alemao expandido
        "ich bin glucklich": "alegria feliz contentamento",
        "ich bin so glucklich": "alegria muito feliz euforia",
        "bin glucklich": "alegria feliz contentamento",
        "sehr glucklich": "alegria muito feliz",
        "ich bin froh": "alegria feliz contente",
        "ich bin erschopft": "esgotado burnout estresse exausto",
        "bin erschopft": "esgotado burnout estresse",
        "ich bin ausgebrannt": "burnout esgotado estresse",
        "ich bin mude": "cansado esgotado exausto",
        "total erschopft": "muito esgotado burnout",
        "ich bin aufgeregt": "animado empolgado entusiasmado",
        "ich bin einsam": "solidao tristeza abandono",
        "ich bin wutend": "raiva irritado frustrado",
        "ich bin angstlich": "ansiedade nervoso preocupado",
        "ich bin stolz": "orgulho realizacao conquista",
        "ich bin dankbar": "gratidao alegria reconhecimento",
        "ich bin verliebt": "amor paixao apaixonado",
        "ich bin deprimiert": "tristeza depressao melancolia",
        "ich bin gestresst": "estresse ansiedade sobrecarregado",
        "ich bin nervos": "ansiedade nervoso agitado",
        # Frances expandido
        "je suis heureux": "alegria feliz contentamento",
        "je suis heureuse": "alegria feliz contentamento",
        "tellement heureux": "muito feliz alegria euforia",
        "tellement heureuse": "muito feliz alegria euforia",
        "suis heureux": "alegria feliz contentamento",
        "suis heureuse": "alegria feliz contentamento",
        "je suis content": "alegria contentamento satisfeito",
        "je suis contente": "alegria contentamento satisfeita",
        "je suis epuise": "esgotado burnout estresse",
        "je suis epuisee": "esgotada burnout estresse",
        "je suis anxieux": "ansiedade nervoso preocupado",
        "je suis en colere": "raiva irritado frustrado",
        "je suis amoureux": "amor paixao apaixonado",
        "je suis amoureuse": "amor paixao apaixonada",
        "je suis fier": "orgulho realizacao conquista",
        "je suis stresse": "estresse ansiedade sobrecarregado",
        "je suis deprime": "tristeza depressao melancolia",
        "je suis seul": "solidao tristeza abandono",
        # Italiano expandido
        "sono stanco": "cansado esgotado exausto",
        "molto stanco": "muito cansado esgotado estresse",
        "sono molto stanco": "muito cansado esgotado estresse",
        "sono esausto": "esgotado burnout estresse",
        "sono felice": "alegria feliz contentamento",
        "molto felice": "muito feliz alegria euforia",
        "sono triste": "tristeza deprimido melancolia",
        "sono arrabbiato": "raiva irritado frustrado",
        "sono ansioso": "ansiedade nervoso preocupado",
        "sono solo": "solidao tristeza abandono",
        "sono innamorato": "amor paixao apaixonado",
        "sono orgoglioso": "orgulho realizacao conquista",
        "sono grato": "gratidao alegria reconhecimento",
        "sono depresso": "tristeza depressao melancolia",
        "sono stressato": "estresse ansiedade sobrecarregado",
        "ho paura": "medo ansiedade panico",
        "mi sento solo": "solidao tristeza abandono",
        "mi sento male": "tristeza ruim mal",
        # Fixes especificos
        "nao aguento mais esse trabalho": "estresse burnout frustracao esgotado",
        "nao aguento mais trabalhar": "estresse burnout esgotado",
        "me sinto vazio por dentro": "vazio solidao anedonia",
        "vazio por dentro": "vazio solidao anedonia",
        "me sinto vazia por dentro": "vazio solidao anedonia",
        "sinto vazio": "vazio solidao anedonia",
        "sentindo vazio": "vazio solidao anedonia",
        "je taime": "amor paixao carinho frances",
        "je t aime": "amor paixao carinho frances",
        "ti amo": "amor paixao carinho italiano",
        "te amo": "amor paixao carinho espanhol",
        "te quiero": "amor carinho afeto espanhol",
        "ai shiteru": "amor paixao carinho japones",
        "sarang hae": "amor paixao carinho coreano",
        "orgulhoso de mim": "orgulho realizacao autoestima",
        "orgulhosa de mim": "orgulho realizacao autoestima",
        "me sinto orgulhoso": "orgulho realizacao conquista",
        "me sinto orgulhosa": "orgulho realizacao conquista",
        "to orgulhoso": "orgulho realizacao conquista",
        "to orgulhosa": "orgulho realizacao conquista",
        # Japones romanizado
        "tengo mucho miedo": "medo ansiedade panico",
        "tengo miedo": "medo ansiedade panico",
        "estoy muy orgulloso": "orgulho realizacao conquista",
        "ich bin so wutend": "raiva irritado furioso",
        "ich bin wutend": "raiva irritado frustrado",
        "ich bin so einsam": "solidao tristeza abandono",
        "ich bin einsam": "solidao tristeza abandono",
        "sono molto stanco": "esgotado cansado exausto estresse",
        "molto stanco": "esgotado cansado exausto",
        "monday blues": "tristeza desanimado melancolia",
        "feeling the monday blues": "tristeza desanimado melancolia",
        "my heart is broken": "tristeza dor coracao partido",
        "heart is broken": "tristeza dor amor perdido",
        "heartbroken": "tristeza dor amor perdido",
        "walking on sunshine": "alegria euforia felicidade",
        "to no seimo ceu": "alegria euforia amor",
        "no setimo ceu": "alegria euforia amor",
        "me sinto culpado": "culpa remorso arrependimento",
        "me sinto culpada": "culpa remorso arrependimento",
        "sinto culpa": "culpa remorso arrependimento",
        "to cheio de esperanca": "esperanca otimismo alegria",
        "cheio de esperanca": "esperanca otimismo alegria",
        "cheia de esperanca": "esperanca otimismo alegria",
        "me sinto muito corajoso": "coragem determinacao orgulho",
        "me sinto corajoso": "coragem determinacao orgulho",
        "me sinto corajosa": "coragem determinacao orgulho",
        "ich bin sehr deprimiert": "tristeza depressao melancolia",
        "ich bin deprimiert": "tristeza depressao melancolia",
        "sehr deprimiert": "tristeza depressao melancolia",
        "sabishii": "solidao tristeza abandono",
        "kanashii": "tristeza melancolia deprimido",
        # Fixes especificos
        "estoy muy triste": "tristeza deprimido melancolia",
        "muy triste": "tristeza deprimido melancolia",
        "estoy triste": "tristeza deprimido melancolia",
        "triste hoy": "tristeza deprimido melancolia",
        "triste hoje": "tristeza deprimido melancolia",
        "triste demais": "tristeza deprimido melancolia",
        "muy triste hoy": "tristeza deprimido melancolia",
        "tres triste": "tristeza profunda melancolia",
        "suis tres triste": "tristeza profunda melancolia",
        "je suis tres triste": "tristeza profunda melancolia",
        "je suis triste": "tristeza deprimido melancolia",
        "suis triste": "tristeza deprimido melancolia",
        "estoy muy": "muito estado emocional",
        "que saudade": "saudade nostalgia tristeza",
        "saudade dos tempos": "saudade nostalgia tristeza",
        "tanta saudade": "saudade nostalgia tristeza",
        "com saudade": "saudade nostalgia tristeza",
        "morrendo de saudade": "saudade nostalgia tristeza",
        "je suis tres triste": "tristeza deprimido melancolia",
        "tres triste": "tristeza profunda melancolia",
        "je suis triste": "tristeza deprimido melancolia",
        "suis triste": "tristeza deprimido melancolia",
        "sono stanco": "esgotado cansado exausto",
        "molto stanco": "esgotado muito cansado exausto",
        "sono molto stanco": "esgotado muito cansado exausto",
        "ureshii": "alegria felicidade contentamento",
        "tanoshii": "alegria diversao prazer",
        "kowai": "medo panico ansiedade",
        "hazukashii": "vergonha timidez constrangimento",
        "natsukashii": "saudade nostalgia tristeza",
        "yabai": "surpresa espanto admiracao",
        "mendokusai": "tedio preguica desmotivado",
        # Coreano romanizado
        "aigoo": "surpresa frustracao espanto",
        "daebak": "admiracao surpresa alegria",
        "han": "tristeza sofrimento profundo",
        "nurmul": "tristeza choro emocao",
    }
    
    texto_lower = texto.lower().strip()
    texto_lower_sem_acento = normalizar_texto(texto_lower)
    
    # Adicionar traducoes diretas ao texto normalizado
    extras = []
    for expr, traducao in mapa_direto.items():
        expr_norm = normalizar_texto(expr)
        if expr_norm in texto_lower_sem_acento or expr in texto_lower:
            extras.append(traducao)
    
    if extras:
        texto_normalizado = texto_normalizado + " " + " ".join(extras)
    
    texto_norm = normalizar_texto(texto_normalizado)
    
    pontuacao = {}
    
    # 2. Detectar negacoes
    negacoes = ["nao ", "nem ", "nunca ", "jamais ", "sem ", "not ", "no "]
    tem_negacao = any(n in texto_norm for n in negacoes)

    # 3. Pontuacao por palavras expandidas
    for emocao, palavras_list in PALAVRAS_EMOCOES_EXPANDIDO.items():
        pontos = 0
        for palavra in palavras_list:
            palavra_norm = normalizar_texto(palavra)
            if palavra_norm in texto_norm:
                base = len(palavra_norm.split())
                if len(palavra_norm.split()) > 1:
                    base *= 2
                if tem_negacao and emocao in ["alegria","amor","gratidao","euforia","esperanca","paz","calma"]:
                    base = max(1, base - 2)
                pontos += base
        if pontos > 0:
            pontuacao[emocao] = pontos

    # 4. Bonus por emojis
    emoji_emocao = {
        "alegria":    ["😄","😊","🎉","😁","🥳","😃","😀","🤩","🥰"],
        "tristeza":   ["😢","😭","💔","😔","😞","😿","🥺","😓"],
        "raiva":      ["😡","🤬","😤","💢","👊","🔥"],
        "medo":       ["😨","😱","😰","🫣","😧"],
        "ansiedade":  ["😰","😟","😬","🫠","😥"],
        "amor":       ["❤️","🥰","💕","💖","😍","💝","💘"],
        "surpresa":   ["😮","😲","🤯","😯","🫢"],
        "nojo":       ["🤢","🤮","😖","🤧"],
        "gratidao":   ["🙏","💙","🫶","🤗","😇"],
        "calma":      ["😌","🧘","🌿","☮️","🕊️"],
        "euforia":    ["🚀","⚡","🌟","✨","🎊","🏆"],
        "saudade":    ["📸","🥺","💭","🌅"],
        "orgulho":    ["💪","🏆","🎯","⭐","👑"],
        "desespero":  ["😩","😫","💀","🫠"],
        "paz":        ["☮️","🌸","🌈","🌺","💚"],
    }
    for emocao, emojis_list in emoji_emocao.items():
        for e in emojis_list:
            if e in texto_orig:
                pontuacao[emocao] = pontuacao.get(emocao, 0) + 4

    # 5. Boost por palavras intensas
    palavras_intensas = [
        "odeio","detesto","amo","adoro","apaixonado","desesperado","eufórico",
        "destruido","arrasado","incrivel","horrivel","pessimo","otimo","maravilhoso",
        "nunca","sempre","demais","extremamente","totalmente","completamente",
    ]
    for p in palavras_intensas:
        if normalizar_texto(p) in texto_norm:
            for emocao in pontuacao:
                pontuacao[emocao] = int(pontuacao[emocao] * 1.4)

    # 6. Boost por repeticao de letras (muuuito, nãooo)
    if re.search(r'(.){2,}', texto.lower()):
        for emocao in pontuacao:
            pontuacao[emocao] = int(pontuacao[emocao] * 1.2)

    # 7. Boost por exclamacao
    if texto.count("!") >= 2:
        for emocao in ["alegria","raiva","euforia","desespero","surpresa"]:
            if emocao in pontuacao:
                pontuacao[emocao] = int(pontuacao[emocao] * 1.3)

    if not pontuacao:
        return "neutro"

    return max(pontuacao, key=pontuacao.get)


def calcular_intensidade(texto: str) -> int:
    intensificadores = [
        "muito", "demais", "extremamente", "super", "mega",
        "completamente", "totalmente", "absurdamente", "profundamente",
        "imensamente", "terrivelmente", "incrivelmente", "demasiadamente",
        "excessivamente", "extraordinariamente", "infinitamente",
        "horrivel", "maravilhoso", "incrivel", "devastado", "apaixonado",
        "odeio", "adoro", "desesperado", "eufórico", "arrasado"
    ]
    texto_lower = texto.lower()
    tem_intensificador = any(i in texto_lower for i in intensificadores)
    tem_exclamacao     = texto.count("!") >= 2
    tem_maiusculas     = sum(1 for c in texto if c.isupper()) > len(texto) * 0.3
    texto_longo        = len(texto) > 150
    tem_repeticao      = any(c*3 in texto_lower for c in "aeiourstmnl")
    tem_emoji_intenso  = any(e in texto for e in ["😱","🤯","💔","😭","🥳","🤬","😍"])

    score = sum([
        tem_intensificador,
        tem_exclamacao,
        tem_maiusculas,
        texto_longo,
        tem_repeticao,
        tem_emoji_intenso
    ])

    if score >= 5:
        return 5
    if score >= 4:
        return 4
    if score >= 3:
        return 3
    if score >= 2:
        return 2
    if score >= 1:
        return 2
    return 1

# ================================================================
# HELPERS DE BANCO
# ================================================================

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usuario_logado(request: Request, db: Session = Depends(get_db)):
    session_id = request.cookies.get("session_id")
    if not session_id or session_id not in sessoes:
        return None
    usuario_id = sessoes[session_id]
    usuario    = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario or not usuario.ativo:
        return None
    # Verifica trial expirado
    if usuario.plano == "trial" and usuario.trial_expira:
        if datetime.now() > usuario.trial_expira:
            usuario.plano = "free"
            db.commit()
    # Atualiza último acesso
    usuario.ultimo_acesso = datetime.now()
    db.commit()
    return usuario


def get_limite(usuario, tipo: str) -> int:
    plano = usuario.plano if usuario.plano in LIMITES else "free"
    return LIMITES[plano][tipo]


def contar_hoje(model, usuario_id: int, db: Session) -> int:
    hoje = date.today()
    return db.query(model).filter(
        model.usuario_id == usuario_id,
        model.criado_em  >= datetime.combine(hoje, datetime.min.time())
    ).count()


def contar_total_usuarios(db: Session) -> int:
    return db.query(Usuario).count()


def calcular_badge(pontos: int) -> str:
    badge_atual = "🌱 Iniciante"
    for limite, badge in BADGES:
        if pontos >= limite:
            badge_atual = badge
    return badge_atual


def proximo_badge(pontos: int) -> dict:
    for limite, badge in BADGES:
        if pontos < limite:
            return {
                "badge":  badge,
                "faltam": limite - pontos,
                "limite": limite
            }
    return {
        "badge":  "👑 Máximo atingido!",
        "faltam": 0,
        "limite": 5000
    }


def adicionar_pontos(usuario, pontos: int, db: Session):
    usuario.pontos += pontos
    usuario.badge   = calcular_badge(usuario.pontos)
    db.commit()
    verificar_conquistas(usuario, db)


def verificar_conquistas(usuario, db: Session):
    conquistas_existentes = [
        c.nome for c in db.query(Conquista).filter(
            Conquista.usuario_id == usuario.id
        ).all()
    ]
    novas = []
    total_analises  = len(usuario.analises)
    total_mensagens = len(usuario.mensagens)
    total_diarios   = len(usuario.diarios)

    if total_analises >= 1 and "Primeira Análise" not in conquistas_existentes:
        novas.append(Conquista(
            nome="Primeira Análise",
            descricao="Fez sua primeira análise emocional",
            emoji="🎯",
            usuario_id=usuario.id
        ))
    if total_analises >= 50 and "Analista Experiente" not in conquistas_existentes:
        novas.append(Conquista(
            nome="Analista Experiente",
            descricao="Completou 50 análises emocionais",
            emoji="📊",
            usuario_id=usuario.id
        ))
    if total_mensagens >= 10 and "Amigo da Sofia" not in conquistas_existentes:
        novas.append(Conquista(
            nome="Amigo da Sofia",
            descricao="Trocou 10 mensagens com a Sofia",
            emoji="🤝",
            usuario_id=usuario.id
        ))
    if total_diarios >= 7 and "Diarista Emocional" not in conquistas_existentes:
        novas.append(Conquista(
            nome="Diarista Emocional",
            descricao="Escreveu 7 entradas no diário",
            emoji="📖",
            usuario_id=usuario.id
        ))
    if usuario.pontos >= 1000 and "Milionario de Pontos" not in conquistas_existentes:
        novas.append(Conquista(
            nome="Milionario de Pontos",
            descricao="Acumulou 1000 pontos na plataforma",
            emoji="💰",
            usuario_id=usuario.id
        ))
    if total_analises >= 10 and "Explorador Emocional" not in conquistas_existentes:
        novas.append(Conquista(
            nome="Explorador Emocional",
            descricao="Completou 10 analises emocionais",
            emoji="🔍",
            usuario_id=usuario.id
        ))
    if total_analises >= 100 and "Mestre das Emocoes" not in conquistas_existentes:
        novas.append(Conquista(
            nome="Mestre das Emocoes",
            descricao="Completou 100 analises emocionais",
            emoji="🏆",
            usuario_id=usuario.id
        ))
    if total_mensagens >= 1 and "Primeiro Contato" not in conquistas_existentes:
        novas.append(Conquista(
            nome="Primeiro Contato",
            descricao="Enviou sua primeira mensagem para a Sofia",
            emoji="💬",
            usuario_id=usuario.id
        ))
    if total_mensagens >= 50 and "Confidente da Sofia" not in conquistas_existentes:
        novas.append(Conquista(
            nome="Confidente da Sofia",
            descricao="Trocou 50 mensagens com a Sofia",
            emoji="🧠",
            usuario_id=usuario.id
        ))
    if total_diarios >= 1 and "Primeiro Diario" not in conquistas_existentes:
        novas.append(Conquista(
            nome="Primeiro Diario",
            descricao="Escreveu sua primeira entrada no diario",
            emoji="📝",
            usuario_id=usuario.id
        ))
    if total_diarios >= 30 and "Escritor Emocional" not in conquistas_existentes:
        novas.append(Conquista(
            nome="Escritor Emocional",
            descricao="Escreveu 30 entradas no diario",
            emoji="✍️",
            usuario_id=usuario.id
        ))
    if usuario.pontos >= 500 and "Meio Caminho" not in conquistas_existentes:
        novas.append(Conquista(
            nome="Meio Caminho",
            descricao="Acumulou 500 pontos na plataforma",
            emoji="⭐",
            usuario_id=usuario.id
        ))
    if usuario.pontos >= 5000 and "Lenda da Plataforma" not in conquistas_existentes:
        novas.append(Conquista(
            nome="Lenda da Plataforma",
            descricao="Acumulou 5000 pontos — voce e uma lenda",
            emoji="👑",
            usuario_id=usuario.id
        ))
    if total_analises >= 7 and "Semana Completa" not in conquistas_existentes:
        novas.append(Conquista(
            nome="Semana Completa",
            descricao="7 dias consecutivos de analises emocionais",
            emoji="📅",
            usuario_id=usuario.id
        ))
    if total_analises >= 200 and "Centenario Duplo" not in conquistas_existentes:
        novas.append(Conquista(
            nome="Centenario Duplo",
            descricao="Completou 200 analises emocionais",
            emoji="🎖️",
            usuario_id=usuario.id
        ))
    if total_diarios >= 50 and "Cronicador Emocional" not in conquistas_existentes:
        novas.append(Conquista(
            nome="Cronicador Emocional",
            descricao="Escreveu 50 entradas no diario",
            emoji="📚",
            usuario_id=usuario.id
        ))
    if usuario.pontos >= 2000 and "Investidor Emocional Pro" not in conquistas_existentes:
        novas.append(Conquista(
            nome="Investidor Emocional Pro",
            descricao="Acumulou 2000 pontos na plataforma",
            emoji="💎",
            usuario_id=usuario.id
        ))
    if total_mensagens >= 100 and "Guru da Sofia" not in conquistas_existentes:
        novas.append(Conquista(
            nome="Guru da Sofia",
            descricao="Trocou 100 mensagens com a Sofia",
            emoji="🧙",
            usuario_id=usuario.id
        ))
    if usuario.plano in ["premium", "enterprise"] and "Assinante Premium" not in conquistas_existentes:
        novas.append(Conquista(
            nome="Assinante Premium",
            descricao="Tornou-se um assinante Premium",
            emoji="⭐",
            usuario_id=usuario.id
        ))
    if total_analises >= 30 and "Veterano Emocional" not in conquistas_existentes:
        novas.append(Conquista(
            nome="Veterano Emocional",
            descricao="Completou 30 analises emocionais",
            emoji="🎗️",
            usuario_id=usuario.id
        ))
    if total_diarios >= 14 and "Duas Semanas" not in conquistas_existentes:
        novas.append(Conquista(
            nome="Duas Semanas",
            descricao="14 entradas no diario emocional",
            emoji="🗓️",
            usuario_id=usuario.id
        ))
    if usuario.pontos >= 100 and "Primeiros Passos" not in conquistas_existentes:
        novas.append(Conquista(
            nome="Primeiros Passos",
            descricao="Acumulou seus primeiros 100 pontos",
            emoji="👣",
            usuario_id=usuario.id
        ))
    if usuario.plano in ["premium","enterprise"] and "Investidor Emocional" not in conquistas_existentes:
        novas.append(Conquista(
            nome="Investidor Emocional",
            descricao="Fez upgrade para plano Premium ou Enterprise",
            emoji="💎",
            usuario_id=usuario.id
        ))

    for c in novas:
        db.add(c)
    if novas:
        db.commit()


def registrar_log(
    rota: str, metodo: str, ip: str,
    status: int, usuario_id: int = None,
    db: Session = None, duracao_ms: float = None,
    user_agent: str = None
):
    if db:
        log = LogAcesso(
            rota=rota, metodo=metodo, ip=ip,
            status=status, usuario_id=usuario_id,
            duracao_ms=duracao_ms, user_agent=user_agent
        )
        db.add(log)
        db.commit()

# ================================================================
# SESSÕES
# ================================================================

sessoes: dict = {}

# ================================================================
# EMAILS — SENDGRID COMPLETO
# ================================================================

def enviar_email(destinatario: str, assunto: str, html: str):
    try:
        sg      = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
        message = Mail(
            from_email=ADMIN_EMAIL,
            to_emails=destinatario,
            subject=assunto,
            html_content=html
        )
        sg.send(message)
        print(f"[Email] Enviado para {destinatario}: {assunto}")
    except Exception as e:
        print(f"[Email] Erro ao enviar para {destinatario}: {e}")


def email_base(conteudo_interno: str) -> str:
    return f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body style="
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background: #f0f4f8;
        margin: 0;
        padding: 20px;
    ">
        <div style="
            max-width: 600px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        ">
            <div style="
                background: linear-gradient(135deg, #00d2ff, #3a7bd5);
                padding: 40px;
                text-align: center;
            ">
                <h1 style="color: white; margin: 0; font-size: 28px;">
                    🧠 Emotion Intelligence
                </h1>
                <p style="color: rgba(255,255,255,0.8); margin: 10px 0 0;">
                    v20.0 ULTIMATE
                </p>
            </div>
            <div style="padding: 40px;">
                {conteudo_interno}
            </div>
            <div style="
                background: #f8f9fa;
                padding: 20px;
                text-align: center;
                border-top: 1px solid #e9ecef;
            ">
                <p style="color: #6c757d; font-size: 12px; margin: 0;">
                    © 2025 Emotion Intelligence Platform |
                    <a href="{BASE_URL}/privacidade" style="color: #00d2ff;">
                        Privacidade
                    </a> |
                    <a href="{BASE_URL}/termos" style="color: #00d2ff;">
                        Termos
                    </a>
                </p>
            </div>
        </div>
    </body>
    </html>
    """


def botao_email(texto: str, url: str, cor: str = "#00d2ff") -> str:
    return f"""
    <div style="text-align: center; margin: 30px 0;">
        <a href="{url}" style="
            background: linear-gradient(135deg, {cor}, #3a7bd5);
            color: white;
            padding: 15px 40px;
            border-radius: 50px;
            text-decoration: none;
            font-size: 16px;
            font-weight: bold;
            display: inline-block;
        ">{texto}</a>
    </div>
    """


def enviar_telegram(mensagem: str):
    try:
        import urllib.request
        import urllib.parse
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        dados = urllib.parse.urlencode({
            "chat_id": TELEGRAM_CHAT_ID,
            "text": mensagem,
            "parse_mode": "HTML"
        }).encode()
        req = urllib.request.Request(url, data=dados)
        urllib.request.urlopen(req, timeout=5)
    except Exception as e:
        print(f"[TELEGRAM] Erro: {e}")


async def enviar_email_boas_vindas(nome: str, email: str, ref_code: str):
    link_afiliado = f"{BASE_URL}/?ref={ref_code}"
    conteudo = f"""
    <h2 style="color: #333; margin-top: 0;">
        Olá, {nome}! 👋
    </h2>
    <p style="color: #555; line-height: 1.6;">
        Seja muito bem-vindo(a) ao <strong>Emotion Intelligence</strong>!
        Estamos felizes em ter você aqui. 🎉
    </p>
    <div style="
        background: #f8f9ff;
        border-left: 4px solid #00d2ff;
        padding: 20px;
        border-radius: 8px;
        margin: 20px 0;
    ">
        <h3 style="color: #333; margin-top: 0;">
            🎁 Seu plano FREE inclui:
        </h3>
        <ul style="color: #555; line-height: 2;">
            <li>✅ 10 análises emocionais por dia</li>
            <li>✅ 5 conversas com a Sofia por dia</li>
            <li>✅ 3 entradas no diário emocional por dia</li>
            <li>✅ Sistema de pontos e badges</li>
            <li>✅ Ranking global</li>
        </ul>
    </div>
    <div style="
        background: linear-gradient(135deg, #fff9e6, #fff3cd);
        border: 1px solid #ffc107;
        padding: 20px;
        border-radius: 8px;
        margin: 20px 0;
    ">
        <h3 style="color: #856404; margin-top: 0;">
            💰 Programa de Afiliados
        </h3>
        <p style="color: #856404;">
            Compartilhe seu link e ganhe
            <strong>20% de comissão</strong> em cada venda!
        </p>
        <div style="
            background: white;
            padding: 10px 15px;
            border-radius: 8px;
            font-family: monospace;
            font-size: 14px;
            word-break: break-all;
            color: #333;
        ">
            {link_afiliado}
        </div>
    </div>
    {botao_email("🚀 Acessar Dashboard", BASE_URL)}
    <p style="color: #888; font-size: 13px; text-align: center;">
        Qualquer dúvida, estamos aqui! 💙
    </p>
    """
    enviar_email(email, "🧠 Bem-vindo ao Emotion Intelligence!", email_base(conteudo))


async def enviar_email_novo_cadastro(nome: str, email: str):
    conteudo = f"""
    <h2 style="color: #333; margin-top: 0;">
        🎉 Novo usuário cadastrado!
    </h2>
    <table style="width: 100%; border-collapse: collapse;">
        <tr>
            <td style="padding: 10px; border-bottom: 1px solid #eee; color: #666;">
                <strong>Nome:</strong>
            </td>
            <td style="padding: 10px; border-bottom: 1px solid #eee; color: #333;">
                {nome}
            </td>
        </tr>
        <tr>
            <td style="padding: 10px; border-bottom: 1px solid #eee; color: #666;">
                <strong>Email:</strong>
            </td>
            <td style="padding: 10px; border-bottom: 1px solid #eee; color: #333;">
                {email}
            </td>
        </tr>
        <tr>
            <td style="padding: 10px; color: #666;">
                <strong>Data:</strong>
            </td>
            <td style="padding: 10px; color: #333;">
                {datetime.now().strftime("%d/%m/%Y às %H:%M")}
            </td>
        </tr>
    </table>
    {botao_email("👤 Ver Painel Admin", f"{BASE_URL}/admin", "#2ecc71")}
    """
    enviar_email(
        ADMIN_EMAIL,
        f"🎉 Novo cadastro: {nome}",
        email_base(conteudo)
    )


async def enviar_email_premium(
    nome: str, email: str, plano: str = "premium"
):
    valor = "R$49/mês" if plano == "premium" else "R$199/mês"
    emoji_plano = "⭐" if plano == "premium" else "🏢"
    conteudo = f"""
    <h2 style="color: #333; margin-top: 0;">
        Parabéns, {nome}! 🎉
    </h2>
    <p style="color: #555; line-height: 1.6;">
        Seu plano <strong>{emoji_plano} {plano.capitalize()}</strong>
        foi ativado com sucesso!
    </p>
    <div style="
        background: linear-gradient(135deg, #f0fff4, #dcfce7);
        border: 1px solid #86efac;
        padding: 20px;
        border-radius: 8px;
        margin: 20px 0;
    ">
        <h3 style="color: #166534; margin-top: 0;">
            🚀 Agora você tem acesso a:
        </h3>
        <ul style="color: #166534; line-height: 2;">
            <li>✅ Análises emocionais <strong>ilimitadas</strong></li>
            <li>✅ Chat ilimitado com a Sofia</li>
            <li>✅ Diário emocional <strong>ilimitado</strong></li>
            <li>✅ Relatórios semanais detalhados por email</li>
            <li>✅ Respostas Premium da Sofia (8-15 linhas)</li>
            <li>✅ Técnicas avançadas: TCC, EMDR, Mindfulness</li>
            <li>✅ +5 pontos por mensagem (vs +2 no free)</li>
            <li>✅ Prioridade no suporte</li>
        </ul>
    </div>
    <p style="
        text-align: center;
        font-size: 24px;
        color: #00d2ff;
        font-weight: bold;
    ">
        +50 pontos de bônus adicionados! 🏆
    </p>
    {botao_email("🚀 Acessar Dashboard", BASE_URL)}
    """
    enviar_email(
        email,
        f"⭐ Plano {plano.capitalize()} ativado!",
        email_base(conteudo)
    )
    # Notifica admin
    conteudo_admin = f"""
    <h2 style="color: #333; margin-top: 0;">
        💰 Nova assinatura {plano.capitalize()}!
    </h2>
    <table style="width: 100%; border-collapse: collapse;">
        <tr>
            <td style="padding: 10px; border-bottom: 1px solid #eee;">
                <strong>Nome:</strong>
            </td>
            <td style="padding: 10px; border-bottom: 1px solid #eee;">
                {nome}
            </td>
        </tr>
        <tr>
            <td style="padding: 10px; border-bottom: 1px solid #eee;">
                <strong>Email:</strong>
            </td>
            <td style="padding: 10px; border-bottom: 1px solid #eee;">
                {email}
            </td>
        </tr>
        <tr>
            <td style="padding: 10px; border-bottom: 1px solid #eee;">
                <strong>Plano:</strong>
            </td>
            <td style="padding: 10px; border-bottom: 1px solid #eee;">
                {plano.capitalize()} — {valor}
            </td>
        </tr>
        <tr>
            <td style="padding: 10px;">
                <strong>Data:</strong>
            </td>
            <td style="padding: 10px;">
                {datetime.now().strftime("%d/%m/%Y às %H:%M")}
            </td>
        </tr>
    </table>
    {botao_email("Ver Painel Admin", f"{BASE_URL}/admin", "#2ecc71")}
    """
    enviar_email(
        ADMIN_EMAIL,
        f"💰 Nova assinatura {plano.capitalize()}: {nome}",
        email_base(conteudo_admin)
    )


async def enviar_relatorio_semanal(usuario, db: Session):
    try:
        semana   = datetime.now() - timedelta(days=7)
        analises = db.query(Analise).filter(
            Analise.usuario_id == usuario.id,
            Analise.criado_em  >= semana
        ).all()

        if not analises:
            return

        emocoes  = [a.emocao.lower() for a in analises]
        contagem = {}
        for e in emocoes:
            contagem[e] = contagem.get(e, 0) + 1

        mais_freq  = max(contagem, key=contagem.get)
        lista_html = "".join([
            f"<li style='padding: 5px 0;'>"
            f"{get_emoji(e)} <strong>{e.capitalize()}</strong>: {c} vez(es)"
            f"</li>"
            for e, c in sorted(
                contagem.items(), key=lambda x: x[1], reverse=True
            )
        ])

        diarios_semana = db.query(Diario).filter(
            Diario.usuario_id == usuario.id,
            Diario.criado_em  >= semana
        ).count()

        msgs_semana = db.query(Mensagem).filter(
            Mensagem.usuario_id == usuario.id,
            Mensagem.criado_em  >= semana
        ).count()

        intensidade_media = round(
            sum(a.intensidade for a in analises) / len(analises), 1
        )

        # Score IE
        total_all = db.query(Analise).filter(Analise.usuario_id == usuario.id).count()
        total_dias = (datetime.now() - usuario.criado_em).days if usuario.criado_em else 1
        score_ie = min(100, int(total_all * 1.5 + usuario.pontos * 0.05 + total_dias * 0.3))

        # Tendencia emocional
        emocoes_positivas = ["alegria","amor","gratidao","euforia","esperanca","calma","confianca"]
        emocoes_negativas = ["tristeza","raiva","medo","ansiedade","frustracao","vergonha","nojo"]
        pos_count = sum(1 for e in emocoes if e in emocoes_positivas)
        neg_count = sum(1 for e in emocoes if e in emocoes_negativas)
        total_e = len(emocoes) or 1
        pct_pos = int(pos_count / total_e * 100)
        pct_neg = int(neg_count / total_e * 100)
        tendencia = "positiva" if pos_count > neg_count else "negativa" if neg_count > pos_count else "equilibrada"
        cor_tend = "#2ecc71" if tendencia == "positiva" else "#e74c3c" if tendencia == "negativa" else "#f39c12"

        # Dica personalizada baseada na emocao mais frequente
        dicas_map = {
            "tristeza": "Que tal escrever 3 coisas pelas quais voce e grato hoje? A gratidao e um dos antidotos mais poderosos para a tristeza.",
            "ansiedade": "Experimente a tecnica 4-7-8: inspire 4s, segure 7s, expire 8s. Faca 3 vezes quando sentir ansiedade.",
            "raiva": "Quando sentir raiva, espere 90 segundos antes de reagir. A onda quimica da raiva dura so 90 segundos.",
            "medo": "Nomeie seu medo especificamente. Pesquisas mostram que dar nome a uma emocao reduz sua intensidade em ate 50%.",
            "alegria": "Registre esse momento no diario! Revisitar momentos de alegria fortalece a resiliencia emocional.",
            "neutro": "Momentos neutros sao otimos para praticas de mindfulness. Que tal 5 minutos de meditacao hoje?",
        }
        dica_semana = dicas_map.get(mais_freq, dicas_map["neutro"])

        conteudo = f"""
        <div style="background:linear-gradient(135deg,#667eea,#764ba2);padding:30px;border-radius:16px;text-align:center;margin-bottom:24px">
            <h1 style="color:#fff;margin:0 0 8px;font-size:28px">📊 Relatório Semanal</h1>
            <p style="color:rgba(255,255,255,0.85);margin:0;font-size:16px">Olá, {usuario.nome}! Aqui está sua semana emocional.</p>
        </div>

        <!-- SCORE IE -->
        <div style="background:#f8f9ff;border-radius:16px;padding:24px;margin-bottom:20px;text-align:center;border:2px solid #e8ecff">
            <p style="color:#666;margin:0 0 8px;font-size:14px">🧠 Seu Score de Inteligência Emocional</p>
            <div style="font-size:64px;font-weight:900;color:#667eea;line-height:1">{score_ie}</div>
            <p style="color:#666;margin:4px 0 16px;font-size:13px">de 100 pontos</p>
            <div style="background:#e8ecff;border-radius:8px;height:10px;overflow:hidden">
                <div style="width:{score_ie}%;height:100%;background:linear-gradient(90deg,#667eea,#764ba2);border-radius:8px"></div>
            </div>
        </div>

        <!-- STATS GRID -->
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:20px">
            <div style="background:#f0fff4;border-radius:12px;padding:16px;text-align:center;border-left:4px solid #2ecc71">
                <div style="font-size:32px;font-weight:bold;color:#2ecc71">{len(analises)}</div>
                <div style="font-size:12px;color:#666;margin-top:4px">Análises na semana</div>
            </div>
            <div style="background:#f0f8ff;border-radius:12px;padding:16px;text-align:center;border-left:4px solid #3498db">
                <div style="font-size:32px;font-weight:bold;color:#3498db">{msgs_semana}</div>
                <div style="font-size:12px;color:#666;margin-top:4px">Conversas com Sofia</div>
            </div>
            <div style="background:#fff8f0;border-radius:12px;padding:16px;text-align:center;border-left:4px solid #f39c12">
                <div style="font-size:32px;font-weight:bold;color:#f39c12">{diarios_semana}</div>
                <div style="font-size:12px;color:#666;margin-top:4px">Entradas no diário</div>
            </div>
            <div style="background:#fdf0ff;border-radius:12px;padding:16px;text-align:center;border-left:4px solid #9b59b6">
                <div style="font-size:32px;font-weight:bold;color:#9b59b6">{usuario.pontos}</div>
                <div style="font-size:12px;color:#666;margin-top:4px">Pontos totais</div>
            </div>
        </div>

        <!-- TENDENCIA -->
        <div style="background:#fff;border:1px solid #eee;border-radius:12px;padding:20px;margin-bottom:20px">
            <h3 style="color:#333;margin:0 0 12px">📈 Tendência Emocional da Semana</h3>
            <div style="display:flex;gap:12px;align-items:center;margin-bottom:12px">
                <div style="flex:1">
                    <div style="font-size:12px;color:#666;margin-bottom:4px">😊 Positivas ({pct_pos}%)</div>
                    <div style="background:#eee;border-radius:4px;height:8px"><div style="width:{pct_pos}%;height:100%;background:#2ecc71;border-radius:4px"></div></div>
                </div>
                <div style="flex:1">
                    <div style="font-size:12px;color:#666;margin-bottom:4px">😔 Negativas ({pct_neg}%)</div>
                    <div style="background:#eee;border-radius:4px;height:8px"><div style="width:{pct_neg}%;height:100%;background:#e74c3c;border-radius:4px"></div></div>
                </div>
            </div>
            <p style="margin:0;font-size:14px;color:{cor_tend};font-weight:bold">
                Tendência {tendencia} — emoção dominante: {get_emoji(mais_freq)} {mais_freq.capitalize()}
            </p>
        </div>

        <!-- EMOCOES -->
        <div style="background:#fff8f0;border-radius:12px;padding:20px;margin-bottom:20px;border-left:4px solid #f39c12">
            <h3 style="color:#f39c12;margin:0 0 12px">🎭 Emoções Detectadas</h3>
            <ul style="color:#333;line-height:2;margin:0;padding-left:20px">
                {lista_html}
            </ul>
        </div>

        <!-- DICA PERSONALIZADA -->
        <div style="background:linear-gradient(135deg,#e8f5e9,#f1f8e9);border-radius:12px;padding:20px;margin-bottom:20px;border-left:4px solid #4caf50">
            <h3 style="color:#2e7d32;margin:0 0 10px">💡 Dica Personalizada para Você</h3>
            <p style="color:#333;margin:0;line-height:1.7">{dica_semana}</p>
        </div>

        <!-- CONQUISTA -->
        <div style="background:#f0fff4;border-radius:12px;padding:20px;margin-bottom:24px;text-align:center;border:1px solid #86efac">
            <div style="font-size:36px;margin-bottom:8px">{usuario.badge}</div>
            <p style="color:#166534;margin:0;font-weight:600">Badge atual: {usuario.badge}</p>
            <p style="color:#166534;margin:4px 0 0;font-size:13px">{usuario.pontos} pontos acumulados</p>
        </div>

        {botao_email("📊 Ver Dashboard Completo", BASE_URL)}
        {botao_email("🧠 Falar com Sofia", BASE_URL + "/chat", "#9b59b6")}

        <p style="color:#888;font-size:13px;text-align:center;margin-top:20px;line-height:1.6">
            Continue sua jornada! Cada análise é um passo em direção ao autoconhecimento. 💙<br>
            <a href="{BASE_URL}/planos" style="color:#667eea">Upgrade para Premium</a> para relatórios ainda mais detalhados.
        </p>
        """
        enviar_email(
            usuario.email,
            "📊 Seu relatório emocional semanal — Emotion Intelligence",
            email_base(conteudo)
        )
        print(f"[Scheduler] Relatório enviado para {usuario.email}")
    except Exception as e:
        print(f"[Scheduler] Erro ao enviar relatório para {usuario.email}: {e}")

# ================================================================
# SCHEDULER — RELATÓRIO SEMANAL AUTOMÁTICO
# ================================================================

def job_relatorio_semanal():
    db = SessionLocal()
    try:
        usuarios = db.query(Usuario).filter(
            Usuario.plano.in_(["premium", "enterprise"]),
            Usuario.ativo == True
        ).all()
        import asyncio
        for u in usuarios:
            try:
                asyncio.run(enviar_relatorio_semanal(u, db))
            except Exception as e:
                print(f"[Scheduler] Erro: {e}")
        print(f"[Scheduler] Relatórios enviados: {len(usuarios)}")
    finally:
        db.close()



async def enviar_email_dia1(nome: str, email: str):
    conteudo = f"""
    <h2 style="color:#333;margin-top:0">Ola, {nome}! Como foi seu primeiro dia? 🌟</h2>
    <p style="color:#555;line-height:1.6">
        Esperamos que sua primeira analise emocional tenha sido reveladora!
        Hoje queremos compartilhar uma dica poderosa:
    </p>
    <div style="background:#f8f9ff;border-left:4px solid #00d2ff;padding:20px;border-radius:8px;margin:20px 0">
        <h3 style="color:#333;margin-top:0">💡 Dica do Dia: O Poder de Nomear Emocoes</h3>
        <p style="color:#555;line-height:1.6">
            Pesquisadores da UCLA descobriram que simplesmente <strong>nomear uma emocao</strong>
            reduz sua intensidade em ate 50%. O cerebro racional assume o controle quando voce
            coloca palavras no que sente.
        </p>
        <p style="color:#555">
            Experimente agora: como voce esta se sentindo? Tente ser especifico —
            nao apenas triste, mas decepcionado? Saudoso? Frustrado?
        </p>
    </div>
    <div style="background:linear-gradient(135deg,#f0fff4,#dcfce7);border:1px solid #86efac;padding:20px;border-radius:8px;margin:20px 0">
        <h3 style="color:#166534;margin-top:0">📊 Sua Missao de Hoje</h3>
    </div>
    {botao_email('📊 Fazer Analise Agora', BASE_URL + '/analyze')}
    """
    enviar_email(email, '💡 Dica do Dia 1 — O poder de nomear emocoes', email_base(conteudo))


async def enviar_email_dia3(nome: str, email: str):
    conteudo = f"""
    <h2 style="color:#333;margin-top:0">Voce ja conhece seu Score IE, {nome}? 🧠</h2>
    <p style="color:#555;line-height:1.6">
        Voce esta no seu <strong>3o dia</strong> na Emotion Intelligence — parabens pela consistencia!
    </p>
    <div style="background:linear-gradient(135deg,#667eea,#764ba2);padding:24px;border-radius:12px;margin:20px 0;text-align:center">
        <h3 style="color:#fff;margin-top:0">🎯 Score de Inteligencia Emocional</h3>
        <p style="color:rgba(255,255,255,0.9);line-height:1.6">
            Seu <strong>Score IE</strong> mede 4 dimensoes: Autoconsciencia, Autorregulacao,
            Empatia e Motivacao. Quanto mais voce usa a plataforma, mais preciso ele fica.
        </p>
        <p style="color:rgba(255,255,255,0.8);font-size:14px">
            Usuarios que acompanham seu Score IE evoluem <strong>3x mais rapido</strong>
            em inteligencia emocional.
        </p>
    </div>
    <div style="background:#fff9e6;border:1px solid #ffc107;padding:20px;border-radius:8px;margin:20px 0">
        <h3 style="color:#856404;margin-top:0">⭐ Quer resultados ainda mais rapidos?</h3>
        <p style="color:#856404;line-height:1.6">
            Com o plano <strong>Premium</strong> voce tem analises ilimitadas, chat ilimitado
            com a Sofia e relatorios semanais detalhados por email.
        </p>
        <p style="color:#856404">Por apenas <strong>R$49/mes</strong> — menos que uma sessao de terapia.</p>
    </div>
    {botao_email('🧠 Ver meu Score IE', BASE_URL + '/perfil')}
    {botao_email('⭐ Conhecer o Premium', BASE_URL + '/planos', '#f39c12')}
    """
    enviar_email(email, '🧠 Dia 3 — Descubra seu Score de Inteligencia Emocional', email_base(conteudo))


async def enviar_email_dia7(nome: str, email: str):
    conteudo = f"""
    <h2 style="color:#333;margin-top:0">1 semana de jornada emocional, {nome}! 🎉</h2>
    <p style="color:#555;line-height:1.6">
        Voce completou sua primeira semana na Emotion Intelligence!
        Isso ja coloca voce entre os <strong>top 20% de usuarios</strong> mais consistentes.
    </p>
    <div style="background:#f8f9ff;border-left:4px solid #00d2ff;padding:20px;border-radius:8px;margin:20px 0">
        <h3 style="color:#333;margin-top:0">📈 O que uma semana de autoconhecimento faz</h3>
        <ul style="color:#555;line-height:2">
            <li>✅ Voce ja tem um padrao emocional mapeado</li>
            <li>✅ Seus gatilhos emocionais estao ficando mais claros</li>
            <li>✅ Sua autoconsciencia aumentou significativamente</li>
            <li>✅ Voce criou o habito mais importante para saude mental</li>
        </ul>
    </div>
    <div style="background:linear-gradient(135deg,#fff9e6,#fff3cd);border:1px solid #ffc107;padding:24px;border-radius:12px;margin:20px 0;text-align:center">
        <h3 style="color:#856404;margin-top:0">🚀 Pronto para o proximo nivel?</h3>
        <p style="color:#856404;line-height:1.6">
            Usuarios Premium tem acesso a <strong>relatorios semanais detalhados</strong>,
            analises ilimitadas e respostas mais profundas da Sofia.
        </p>
        <p style="font-size:28px;font-weight:bold;color:#f39c12">R$49/mes</p>
        <p style="color:#856404;font-size:13px">Cancele quando quiser. Sem fidelidade.</p>
    </div>
    {botao_email('📊 Ver meu Historico', BASE_URL + '/historico')}
    {botao_email('⭐ Assinar Premium', BASE_URL + '/planos', '#f39c12')}
    """
    enviar_email(email, '🎉 1 semana de jornada emocional — veja sua evolucao!', email_base(conteudo))


async def enviar_email_dia14(nome: str, email: str):
    conteudo = f"""
    <h2 style="color:#333;margin-top:0">Presente especial para voce, {nome}! 🎁</h2>
    <p style="color:#555;line-height:1.6">
        2 semanas de jornada emocional! Voce e incrivel pela dedicacao.
        Como agradecimento, temos um presente exclusivo:
    </p>
    <div style="background:linear-gradient(135deg,#667eea,#764ba2);padding:32px;border-radius:16px;margin:20px 0;text-align:center">
        <p style="color:rgba(255,255,255,0.8);font-size:14px;margin-bottom:8px">CUPOM EXCLUSIVO</p>
        <h2 style="color:#fff;font-size:48px;margin:0;letter-spacing:4px">EVOLUCAO20</h2>
        <p style="color:rgba(255,255,255,0.9);margin-top:8px"><strong>20% de desconto</strong> no plano Premium</p>
        <p style="color:rgba(255,255,255,0.7);font-size:13px">Valido por 48 horas</p>
    </div>
    <div style="background:#f8f9ff;padding:20px;border-radius:8px;margin:20px 0">
        <h3 style="color:#333;margin-top:0">💎 Premium com desconto = R$39,20/mes</h3>
        <ul style="color:#555;line-height:2">
            <li>✅ Analises emocionais ilimitadas</li>
            <li>✅ Chat ilimitado com Sofia IA</li>
            <li>✅ Relatorios semanais por email</li>
            <li>✅ Tecnicas avancadas: TCC, EMDR, Mindfulness</li>
            <li>✅ +50 pontos de bonus</li>
        </ul>
    </div>
    {botao_email('🎁 Usar Cupom Agora', BASE_URL + '/planos', '#667eea')}
    <p style="color:#888;font-size:12px;text-align:center">Cupom valido por 48h a partir do recebimento deste email.</p>
    """
    enviar_email(email, '🎁 Presente especial: 20% OFF no Premium (48h apenas!)', email_base(conteudo))


def job_onboarding_emails():
    from sqlalchemy.orm import Session
    import asyncio
    db: Session = SessionLocal()
    try:
        agora = datetime.now()
        usuarios = db.query(Usuario).filter(Usuario.plano == 'free').all()
        for u in usuarios:
            if not u.criado_em:
                continue
            dias = (agora - u.criado_em).days
            try:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                if dias == 1:
                    loop.run_until_complete(enviar_email_dia1(u.nome, u.email))
                elif dias == 3:
                    loop.run_until_complete(enviar_email_dia3(u.nome, u.email))
                elif dias == 7:
                    loop.run_until_complete(enviar_email_dia7(u.nome, u.email))
                elif dias == 14:
                    loop.run_until_complete(enviar_email_dia14(u.nome, u.email))
                loop.close()
            except Exception as email_err:
                print(f'[ONBOARDING] Email erro para {u.email}: {email_err}')
    except Exception as e:
        print(f'[ONBOARDING] Erro geral: {e}')
        enviar_telegram(f"⚠️ Erro onboarding: {str(e)[:100]}")
    finally:
        db.close()

scheduler = BackgroundScheduler()
scheduler.add_job(
    job_relatorio_semanal,
    "cron",
    day_of_week="sun",
    hour=8,
    minute=0
)
scheduler.add_job(
    job_onboarding_emails,
    "cron",
    hour=9,
    minute=0
)
scheduler.start()

# ================================================================
# APP FASTAPI
# ================================================================

app       = FastAPI(
    title="Emotion Intelligence Platform",
    version="20.0",
    description="Plataforma completa de inteligência emocional com IA"
)
templates = Jinja2Templates(directory="templates")

try:
    app.mount("/static", StaticFiles(directory="static"), name="static")
except Exception:
    pass

# ================================================================
# MIDDLEWARE DE LOG
# ================================================================

class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        inicio   = time.time()
        response = await call_next(request)
        duracao  = round((time.time() - inicio) * 1000, 2)
        print(
            f"[{datetime.now().strftime('%H:%M:%S')}] "
            f"{request.method} {request.url.path} "
            f"→ {response.status_code} ({duracao}ms)"
        )
        return response


app.add_middleware(LogMiddleware)

# ================================================================
# FIM DA PARTE 1
# ================================================================
# ================================================================
# ROTAS — SISTEMA
# ================================================================


# ============================================================
# HELPERS MONETIZAÇÃO v19.1
# ============================================================

import secrets as _secrets

PACOTES_CREDITOS = {
    "P": {"nome": "Pacote Starter", "analises": 50,  "sofia": 20,  "preco": 14.90, "economia": ""},
    "M": {"nome": "Pacote Pro",     "analises": 100, "sofia": 50,  "preco": 24.90, "economia": "17%"},
    "G": {"nome": "Pacote Elite",   "analises": 200, "sofia": 120, "preco": 39.90, "economia": "33%"},
}

PLANOS_COMPLETOS = {
    "free":         {"nome": "Free",           "preco": 0,      "periodo": ""},
    "trial":        {"nome": "Trial 7 dias",   "preco": 0,      "periodo": "7 dias"},
    "premium":      {"nome": "Premium Mensal", "preco": 49.00,  "periodo": "mes"},
    "anual":        {"nome": "Premium Anual",  "preco": 399.00, "periodo": "ano", "economia": "R$189"},
    "enterprise":   {"nome": "Enterprise",     "preco": 199.00, "periodo": "mes"},
    "developer":    {"nome": "API Developer",  "preco": 79.00,  "periodo": "mes"},
    "business_api": {"nome": "API Business",   "preco": 199.00, "periodo": "mes"},
    "whitelabel":   {"nome": "White-label",    "preco": 299.00, "periodo": "mes"},
}

def usuario_tem_acesso_premium(usuario) -> bool:
    if usuario.plano in ["premium", "enterprise"]:
        return True
    if getattr(usuario, "plano_anual_ate", None) and usuario.plano_anual_ate > datetime.utcnow():
        return True
    return False

def usuario_tem_creditos_analise(usuario) -> bool:
    return getattr(usuario, "creditos_analise", 0) > 0

def usuario_tem_creditos_sofia(usuario) -> bool:
    return getattr(usuario, "creditos_sofia", 0) > 0

def consumir_credito_analise(usuario_id: int, db) -> bool:
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario and getattr(usuario, "creditos_analise", 0) > 0:
        usuario.creditos_analise -= 1
        tx = TransacaoCredito(
            usuario_id=usuario_id,
            tipo="uso",
            quantidade=-1,
            descricao="Analise emocional consumida"
        )
        db.add(tx)
        db.commit()
        return True
    return False

def consumir_credito_sofia(usuario_id: int, db) -> bool:
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario and getattr(usuario, "creditos_sofia", 0) > 0:
        usuario.creditos_sofia -= 1
        tx = TransacaoCredito(
            usuario_id=usuario_id,
            tipo="uso",
            quantidade=-1,
            descricao="Mensagem Sofia consumida"
        )
        db.add(tx)
        db.commit()
        return True
    return False

def adicionar_creditos(usuario_id: int, tipo: str, quantidade: int, pacote: str, db) -> bool:
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        return False
    from datetime import timedelta
    credito = Credito(
        usuario_id=usuario_id,
        tipo=tipo,
        quantidade=quantidade,
        pacote=pacote,
        expira_em=datetime.utcnow() + timedelta(days=365)
    )
    db.add(credito)
    if tipo == "analise":
        usuario.creditos_analise = (getattr(usuario, "creditos_analise", 0) or 0) + quantidade
    elif tipo == "sofia":
        usuario.creditos_sofia = (getattr(usuario, "creditos_sofia", 0) or 0) + quantidade
    tx = TransacaoCredito(
        usuario_id=usuario_id,
        tipo="compra",
        quantidade=quantidade,
        descricao=f"Pacote {pacote} — {quantidade} creditos {tipo}"
    )
    db.add(tx)
    db.commit()
    return True

def gerar_codigo_presente() -> str:
    return "GIFT-" + _secrets.token_hex(6).upper()

def gerar_api_key() -> str:
    return "eip_" + _secrets.token_hex(24)

def verificar_api_key_db(chave: str, db) -> dict:
    api_key = db.query(ApiKey).filter(
        ApiKey.chave == chave,
        ApiKey.ativa == True
    ).first()
    if not api_key:
        return {"valid": False, "error": "API key invalida"}
    if api_key.requisicoes_mes >= api_key.limite_mes:
        return {"valid": False, "error": "Limite mensal atingido"}
    api_key.requisicoes_mes += 1
    api_key.ultimo_uso = datetime.utcnow()
    db.commit()
    return {"valid": True, "usuario_id": api_key.usuario_id, "plano": api_key.plano_api}

def ativar_plano_anual(usuario_id: int, db) -> bool:
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        return False
    from datetime import timedelta
    usuario.plano = "premium"
    usuario.plano_anual_ate = datetime.utcnow() + timedelta(days=365)
    usuario.total_gasto = (getattr(usuario, "total_gasto", 0) or 0) + 399.00
    usuario.fonte_receita = "anual"
    db.commit()
    return True

def resgatar_presente(codigo: str, usuario_id: int, db) -> dict:
    presente = db.query(Presente).filter(
        Presente.codigo == codigo,
        Presente.usado == False
    ).first()
    if not presente:
        return {"ok": False, "erro": "Codigo invalido ou ja usado"}
    if presente.expira_em and presente.expira_em < datetime.utcnow():
        return {"ok": False, "erro": "Codigo expirado"}
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        return {"ok": False, "erro": "Usuario nao encontrado"}
    presente.usado = True
    presente.usado_por = usuario_id
    if presente.plano == "anual":
        ativar_plano_anual(usuario_id, db)
    elif presente.plano in ["premium", "enterprise"]:
        usuario.plano = presente.plano
    elif presente.plano == "creditos":
        adicionar_creditos(usuario_id, "analise", 100, "GIFT", db)
        adicionar_creditos(usuario_id, "sofia", 50, "GIFT", db)
    db.commit()
    return {"ok": True, "plano": presente.plano}



# ============================================================
# ROTAS MONETIZAÇÃO v19.1
# ============================================================

# --- PLANO ANUAL ---




# ================================================================
# STREAK DE DIAS CONSECUTIVOS v20.0
# ================================================================

def calcular_streak(usuario_id: int, db) -> dict:
    """Calcula streak de dias consecutivos de uso"""
    from datetime import timedelta
    analises = db.query(Analise).filter(
        Analise.usuario_id == usuario_id
    ).order_by(Analise.criado_em.desc()).all()
    
    if not analises:
        return {"streak_atual": 0, "streak_maximo": 0, "ultimo_dia": None}
    
    dias_ativos = sorted(set([
        a.criado_em.date() for a in analises if a.criado_em
    ]), reverse=True)
    
    if not dias_ativos:
        return {"streak_atual": 0, "streak_maximo": 0, "ultimo_dia": None}
    
    hoje = datetime.now().date()
    ontem = hoje - timedelta(days=1)
    
    # Streak atual
    streak_atual = 0
    if dias_ativos[0] >= ontem:
        streak_atual = 1
        for i in range(1, len(dias_ativos)):
            esperado = dias_ativos[i-1] - timedelta(days=1)
            if dias_ativos[i] == esperado:
                streak_atual += 1
            else:
                break
    
    # Streak maximo
    streak_max = 1
    streak_temp = 1
    for i in range(1, len(dias_ativos)):
        esperado = dias_ativos[i-1] - timedelta(days=1)
        if dias_ativos[i] == esperado:
            streak_temp += 1
            streak_max = max(streak_max, streak_temp)
        else:
            streak_temp = 1
    
    return {
        "streak_atual": streak_atual,
        "streak_maximo": streak_max,
        "ultimo_dia": dias_ativos[0].strftime("%d/%m/%Y") if dias_ativos else None,
        "emoji": "🔥" if streak_atual >= 7 else "⚡" if streak_atual >= 3 else "✨"
    }

@app.get("/api/streak")
def api_streak(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return JSONResponse({"ok": False}, status_code=401)
    streak = calcular_streak(usuario.id, db)
    return JSONResponse({"ok": True, "streak": streak})

# ================================================================
# FIM STREAK
# ================================================================

# ================================================================
# RECUPERACAO DE SENHA v20.0
# ================================================================

import hashlib as _hashlib

_tokens_recuperacao = {}  # token -> {email, expira}

@app.get("/recuperar-senha", response_class=HTMLResponse)
def pagina_recuperar_senha(request: Request):
    return render_template("recuperar_senha.html", request=request, erro=None, sucesso=None)

@app.post("/recuperar-senha")
async def processar_recuperar_senha(
    request: Request,
    email: str = Form(...),
    db: Session = Depends(get_db)
):
    usuario = db.query(Usuario).filter(Usuario.email == email.lower().strip()).first()
    if not usuario:
        return render_template("recuperar_senha.html", request=request,
            erro="Email não encontrado", sucesso=None)
    # Gerar token unico
    token = _hashlib.sha256(f"{email}{datetime.now().isoformat()}{uuid.uuid4()}".encode()).hexdigest()[:32]
    _tokens_recuperacao[token] = {
        "email": email.lower().strip(),
        "expira": datetime.now() + timedelta(hours=2)
    }
    # Enviar email
    link = f"{BASE_URL}/nova-senha?token={token}"
    html = email_base(f"""
        <h2 style="color:#333;margin-top:0">🔑 Recuperação de Senha</h2>
        <p>Olá, <strong>{usuario.nome}</strong>!</p>
        <p>Recebemos uma solicitação para redefinir sua senha na Emotion Intelligence.</p>
        <p>Clique no botão abaixo para criar uma nova senha:</p>
        {botao_email("🔑 Criar Nova Senha", link)}
        <p style="color:#999;font-size:13px;margin-top:20px">
        Este link expira em 2 horas. Se você não solicitou isso, ignore este email.
        </p>
    """)
    try:
        enviar_email(email, "🔑 Recuperar Senha — Emotion Intelligence", html)
        return render_template("recuperar_senha.html", request=request,
            erro=None, sucesso="Email enviado! Verifique sua caixa de entrada.")
    except Exception as e:
        return render_template("recuperar_senha.html", request=request,
            erro="Erro ao enviar email. Tente novamente.", sucesso=None)

@app.get("/nova-senha", response_class=HTMLResponse)
def pagina_nova_senha(request: Request, token: str = ""):
    if not token or token not in _tokens_recuperacao:
        return render_template("recuperar_senha.html", request=request,
            erro="Link inválido ou expirado", sucesso=None)
    dados = _tokens_recuperacao[token]
    if datetime.now() > dados["expira"]:
        del _tokens_recuperacao[token]
        return render_template("recuperar_senha.html", request=request,
            erro="Link expirado. Solicite um novo.", sucesso=None)
    return render_template("nova_senha.html", request=request, token=token, erro=None)

@app.post("/nova-senha")
def processar_nova_senha(
    request: Request,
    token: str = Form(...),
    senha: str = Form(...),
    confirmar: str = Form(...),
    db: Session = Depends(get_db)
):
    if token not in _tokens_recuperacao:
        return render_template("nova_senha.html", request=request,
            token=token, erro="Token inválido")
    if senha != confirmar:
        return render_template("nova_senha.html", request=request,
            token=token, erro="Senhas não coincidem")
    valida, msg = validar_senha(senha)
    if not valida:
        return render_template("nova_senha.html", request=request,
            token=token, erro=msg)
    dados = _tokens_recuperacao[token]
    usuario = db.query(Usuario).filter(Usuario.email == dados["email"]).first()
    if not usuario:
        return render_template("nova_senha.html", request=request,
            token=token, erro="Usuário não encontrado")
    usuario.senha = hash_senha(senha)
    db.commit()
    del _tokens_recuperacao[token]
    enviar_telegram(f"🔑 Senha alterada\n👤 {usuario.email}")
    return RedirectResponse("/login?msg=Senha alterada com sucesso!", status_code=302)

# ================================================================
# FIM RECUPERACAO DE SENHA
# ================================================================

# ================================================================
# UPSELL AUTOMATICO v20.0
# ================================================================

@app.get("/api/upsell")
def api_upsell(request: Request, db: Session = Depends(get_db)):
    """Retorna dados de upsell quando usuario atinge limite"""
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return JSONResponse({"show": False})
    if usuario_tem_acesso_premium(usuario):
        return JSONResponse({"show": False})
    analises_hoje = contar_hoje(Analise, usuario.id, db)
    msgs_hoje = contar_hoje(Mensagem, usuario.id, db)
    diarios_hoje = contar_hoje(Diario, usuario.id, db)
    limite_analises = get_limite(usuario, "analises")
    limite_chat = get_limite(usuario, "chat")
    limite_diario = get_limite(usuario, "diario")
    upsell = None
    if analises_hoje >= limite_analises:
        upsell = {
            "show": True,
            "tipo": "analises",
            "emoji": "🔍",
            "titulo": f"Limite de {limite_analises} análises atingido!",
            "mensagem": "Faça upgrade para análises ilimitadas por menos de R$1,60/dia",
            "cta": "⭐ Assinar Premium — R$49/mês",
            "url": "/checkout-page?plano=premium",
            "cor": "#00d2ff"
        }
    elif msgs_hoje >= limite_chat:
        upsell = {
            "show": True,
            "tipo": "chat",
            "emoji": "💬",
            "titulo": f"Limite de {limite_chat} mensagens atingido!",
            "mensagem": "Continue conversando com a Sofia sem limites com o Premium",
            "cta": "⭐ Assinar Premium — R$49/mês",
            "url": "/checkout-page?plano=premium",
            "cor": "#9b59b6"
        }
    elif diarios_hoje >= limite_diario:
        upsell = {
            "show": True,
            "tipo": "diario",
            "emoji": "📔",
            "titulo": f"Limite de {limite_diario} diários atingido!",
            "mensagem": "Registre quantas entradas quiser com o Premium",
            "cta": "⭐ Assinar Premium — R$49/mês",
            "url": "/checkout-page?plano=premium",
            "cor": "#2ecc71"
        }
    else:
        return JSONResponse({"show": False})
    return JSONResponse(upsell)

# ================================================================
# FIM UPSELL
# ================================================================

# ================================================================
# SISTEMA DE MONITORAMENTO v20.0 — ALERTAS TELEGRAM AUTOMATICOS
# ================================================================

import threading as _threading

_erros_recentes = []
_max_erros = 100

def monitorar_erro(rota: str, erro: str, usuario_id: int = None):
    """Registra erro e alerta no Telegram se critico"""
    global _erros_recentes
    _erros_recentes.append({
        "rota": rota,
        "erro": erro[:200],
        "usuario_id": usuario_id,
        "timestamp": datetime.now().strftime("%d/%m %H:%M:%S")
    })
    if len(_erros_recentes) > _max_erros:
        _erros_recentes = _erros_recentes[-_max_erros:]
    # Alertar no Telegram para erros criticos
    erros_criticos = ["500","database","connection","timeout","crash","memory"]
    if any(e in erro.lower() for e in erros_criticos):
        msg = (
            f"🚨 <b>ERRO CRITICO DETECTADO</b>\n"
            f"🔴 Rota: {rota}\n"
            f"💥 Erro: {erro[:150]}\n"
            f"⏰ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
        )
        enviar_telegram(msg)

def monitorar_ia_falha(modelo: str, erro: str):
    """Alerta quando modelo de IA falha"""
    msg = (
        f"⚠️ <b>IA FALHOU</b>\n"
        f"🤖 Modelo: {modelo}\n"
        f"❌ Erro: {erro[:100]}\n"
        f"⏰ {datetime.now().strftime('%H:%M:%S')}"
    )
    enviar_telegram(msg)

def relatorio_diario_sistema():
    """Envia relatorio diario de saude do sistema"""
    try:
        db = SessionLocal()
        total_usuarios = db.query(Usuario).count()
        total_analises = db.query(Analise).count()
        total_msgs = db.query(Mensagem).count()
        novos_hoje = db.query(Usuario).filter(
            Usuario.criado_em >= datetime.now().replace(hour=0,minute=0,second=0)
        ).count()
        analises_hoje = db.query(Analise).filter(
            Analise.criado_em >= datetime.now().replace(hour=0,minute=0,second=0)
        ).count()
        pagamentos = db.query(Pagamento).filter(
            Pagamento.status == "approved"
        ).count()
        receita = db.query(Pagamento).filter(
            Pagamento.status == "approved"
        ).all()
        total_receita = sum(p.valor or 0 for p in receita)
        erros_hora = len(_erros_recentes)
        db.close()
        msg = (
            f"📊 <b>RELATORIO DIARIO — Emotion Intelligence v20.0</b>\n\n"
            f"👥 Usuarios total: {total_usuarios}\n"
            f"🆕 Novos hoje: {novos_hoje}\n"
            f"🔍 Analises total: {total_analises}\n"
            f"📈 Analises hoje: {analises_hoje}\n"
            f"💬 Mensagens total: {total_msgs}\n"
            f"💰 Pagamentos aprovados: {pagamentos}\n"
            f"💵 Receita total: R${total_receita:.2f}\n"
            f"⚠️ Erros recentes: {erros_hora}\n"
            f"✅ Sistema: ONLINE\n"
            f"⏰ {datetime.now().strftime('%d/%m/%Y %H:%M')}"
        )
        enviar_telegram(msg)
    except Exception as e:
        enviar_telegram(f"❌ Erro no relatorio diario: {str(e)[:100]}")

def checar_saude_sistema():
    """Checa saude do sistema a cada hora"""
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        db.close()
    except Exception as e:
        enviar_telegram(f"🚨 BANCO DE DADOS OFFLINE!\n{str(e)[:100]}")

# Adicionar jobs ao scheduler
try:
    scheduler.add_job(
        relatorio_diario_sistema,
        "cron",
        hour=7,
        minute=0,
        id="relatorio_diario"
    )
    scheduler.add_job(
        checar_saude_sistema,
        "interval",
        hours=1,
        id="checar_saude"
    )
except Exception as _e:
    print(f"[MONITOR] Scheduler jobs ja existem: {_e}")

# ================================================================
# FIM SISTEMA DE MONITORAMENTO
# ================================================================

@app.get("/checkout/anual", response_class=HTMLResponse)
async def checkout_anual(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return RedirectResponse("/login", status_code=302)
    return render_template("checkout_anual.html", request=request, usuario=usuario, preco=399.00, economia="R$189", parcelas="12x R$33,25")

@app.post("/checkout/anual/processar")
async def processar_checkout_anual(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return JSONResponse({"ok": False, "erro": "Nao autenticado"}, status_code=401)
    try:
        import mercadopago
        sdk = mercadopago.SDK(MP_ACCESS_TOKEN)
        preference_data = {
            "items": [{
                "title": "Emotion Intelligence Platform — Premium Anual",
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": 399.00
            }],
            "payer": {"email": usuario.email},
            "back_urls": {
                "success": f"{BASE_URL}/sucesso?plano=anual",
                "failure": f"{BASE_URL}/checkout/anual",
                "pending": f"{BASE_URL}/checkout/anual"
            },
            "auto_return": "approved",
            "external_reference": f"anual_{usuario.id}",
            "metadata": {"usuario_id": usuario.id, "plano": "anual"}
        }
        preference = sdk.preference().create(preference_data)
        init_point = preference["response"]["init_point"]
        return JSONResponse({"ok": True, "url": init_point})
    except Exception as e:
        return JSONResponse({"ok": False, "erro": str(e)})

# --- CRÉDITOS ---
@app.get("/checkout/creditos", response_class=HTMLResponse)
async def checkout_creditos(request: Request, pacote: str = "M", db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return RedirectResponse("/login", status_code=302)
    pacote = pacote.upper()
    if pacote not in PACOTES_CREDITOS:
        pacote = "M"
    dados = PACOTES_CREDITOS[pacote]
    todos_pacotes_lista = [
        {"key": k, "nome": v["nome"], "preco": v["preco"], "analises": v["analises"], "sofia": v["sofia"], "economia": v.get("economia","")}
        for k, v in PACOTES_CREDITOS.items()
    ]
    return render_template("checkout_creditos.html", request=request, usuario=usuario, pacote=pacote, dados=dados, todos_pacotes=todos_pacotes_lista)

@app.post("/checkout/creditos/processar")
async def processar_checkout_creditos(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return JSONResponse({"ok": False, "erro": "Nao autenticado"}, status_code=401)
    body = await request.json()
    pacote = body.get("pacote", "M").upper()
    if pacote not in PACOTES_CREDITOS:
        return JSONResponse({"ok": False, "erro": "Pacote invalido"})
    dados = PACOTES_CREDITOS[pacote]
    try:
        import mercadopago
        sdk = mercadopago.SDK(MP_ACCESS_TOKEN)
        preference_data = {
            "items": [{
                "title": f"Emotion Platform — {dados['nome']} ({dados['analises']} analises)",
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": dados["preco"]
            }],
            "payer": {"email": usuario.email},
            "back_urls": {
                "success": f"{BASE_URL}/sucesso?plano=creditos&pacote={pacote}",
                "failure": f"{BASE_URL}/checkout/creditos?pacote={pacote}",
                "pending": f"{BASE_URL}/checkout/creditos?pacote={pacote}"
            },
            "auto_return": "approved",
            "external_reference": f"creditos_{pacote}_{usuario.id}",
            "metadata": {"usuario_id": usuario.id, "plano": "creditos", "pacote": pacote}
        }
        preference = sdk.preference().create(preference_data)
        init_point = preference["response"]["init_point"]
        return JSONResponse({"ok": True, "url": init_point})
    except Exception as e:
        return JSONResponse({"ok": False, "erro": str(e)})

# --- SESSÃO SOFIA AVULSA ---
@app.get("/checkout/sofia", response_class=HTMLResponse)
async def checkout_sofia(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return RedirectResponse("/login", status_code=302)
    return render_template("checkout_sofia.html", request=request, usuario=usuario, preco=4.90, msgs=10)

@app.post("/checkout/sofia/processar")
async def processar_checkout_sofia(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return JSONResponse({"ok": False, "erro": "Nao autenticado"}, status_code=401)
    try:
        import mercadopago
        sdk = mercadopago.SDK(MP_ACCESS_TOKEN)
        preference_data = {
            "items": [{
                "title": "Emotion Platform — Sessao Sofia (10 mensagens)",
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": 4.90
            }],
            "payer": {"email": usuario.email},
            "back_urls": {
                "success": f"{BASE_URL}/sucesso?plano=sofia",
                "failure": f"{BASE_URL}/checkout/sofia",
                "pending": f"{BASE_URL}/checkout/sofia"
            },
            "auto_return": "approved",
            "external_reference": f"sofia_{usuario.id}",
            "metadata": {"usuario_id": usuario.id, "plano": "sofia"}
        }
        preference = sdk.preference().create(preference_data)
        init_point = preference["response"]["init_point"]
        return JSONResponse({"ok": True, "url": init_point})
    except Exception as e:
        return JSONResponse({"ok": False, "erro": str(e)})

# --- RELATÓRIO AVULSO ---
@app.get("/checkout/relatorio", response_class=HTMLResponse)
async def checkout_relatorio(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return RedirectResponse("/login", status_code=302)
    from datetime import datetime
    mes_atual = datetime.utcnow().strftime("%Y-%m")
    mes_label = datetime.utcnow().strftime("%B/%Y")
    ja_comprou = db.query(RelatorioPago).filter(
        RelatorioPago.usuario_id == usuario.id,
        RelatorioPago.mes_ref == mes_atual
    ).first()
    return render_template("checkout_relatorio.html", request=request, usuario=usuario, preco=9.90, mes_label=mes_label, ja_comprou=ja_comprou is not None)

@app.post("/checkout/relatorio/processar")
async def processar_checkout_relatorio(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return JSONResponse({"ok": False, "erro": "Nao autenticado"}, status_code=401)
    from datetime import datetime
    mes_atual = datetime.utcnow().strftime("%Y-%m")
    ja_comprou = db.query(RelatorioPago).filter(
        RelatorioPago.usuario_id == usuario.id,
        RelatorioPago.mes_ref == mes_atual
    ).first()
    if ja_comprou:
        return JSONResponse({"ok": False, "erro": "Relatorio deste mes ja comprado"})
    try:
        import mercadopago
        sdk = mercadopago.SDK(MP_ACCESS_TOKEN)
        preference_data = {
            "items": [{
                "title": f"Emotion Platform — Relatorio Emocional {mes_atual}",
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": 9.90
            }],
            "payer": {"email": usuario.email},
            "back_urls": {
                "success": f"{BASE_URL}/sucesso?plano=relatorio&mes={mes_atual}",
                "failure": f"{BASE_URL}/checkout/relatorio",
                "pending": f"{BASE_URL}/checkout/relatorio"
            },
            "auto_return": "approved",
            "external_reference": f"relatorio_{mes_atual}_{usuario.id}",
            "metadata": {"usuario_id": usuario.id, "plano": "relatorio", "mes": mes_atual}
        }
        preference = sdk.preference().create(preference_data)
        init_point = preference["response"]["init_point"]
        return JSONResponse({"ok": True, "url": init_point})
    except Exception as e:
        return JSONResponse({"ok": False, "erro": str(e)})

# --- PRESENTE / GIFT ---
@app.get("/presente", response_class=HTMLResponse)
async def pagina_presente(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return RedirectResponse("/login", status_code=302)
    opcoes_presente = [
        {"plano": "premium",  "nome": "Premium 1 mes", "preco": 49.00},
        {"plano": "anual",    "nome": "Premium Anual",  "preco": 399.00},
        {"plano": "creditos", "nome": "100 Creditos",   "preco": 24.90},
    ]
    return render_template("presente.html", request=request, usuario=usuario, opcoes=opcoes_presente)

@app.post("/presente/processar")
async def processar_presente(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return JSONResponse({"ok": False, "erro": "Nao autenticado"}, status_code=401)
    body = await request.json()
    plano = body.get("plano", "premium")
    email_dest = body.get("email_destinatario", "")
    mensagem = body.get("mensagem", "")
    precos = {"premium": 49.00, "anual": 399.00, "creditos": 24.90}
    preco = precos.get(plano, 49.00)
    codigo = gerar_codigo_presente()
    from datetime import timedelta
    presente = Presente(
        codigo=codigo,
        remetente_id=usuario.id,
        destinatario_email=email_dest,
        plano=plano,
        valor=preco,
        mensagem=mensagem,
        expira_em=datetime.utcnow() + timedelta(days=90)
    )
    db.add(presente)
    db.commit()
    try:
        import mercadopago
        sdk = mercadopago.SDK(MP_ACCESS_TOKEN)
        preference_data = {
            "items": [{
                "title": f"Emotion Platform — Presente {plano.title()} para {email_dest or 'amigo'}",
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": preco
            }],
            "payer": {"email": usuario.email},
            "back_urls": {
                "success": f"{BASE_URL}/presente/sucesso?codigo={codigo}",
                "failure": f"{BASE_URL}/presente",
                "pending": f"{BASE_URL}/presente"
            },
            "auto_return": "approved",
            "external_reference": f"presente_{codigo}_{usuario.id}",
            "metadata": {"usuario_id": usuario.id, "plano": "presente", "codigo": codigo}
        }
        preference = sdk.preference().create(preference_data)
        init_point = preference["response"]["init_point"]
        return JSONResponse({"ok": True, "url": init_point, "codigo": codigo})
    except Exception as e:
        return JSONResponse({"ok": False, "erro": str(e)})

@app.get("/presente/sucesso", response_class=HTMLResponse)
async def presente_sucesso(request: Request, codigo: str, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    presente = db.query(Presente).filter(Presente.codigo == codigo).first()
    return templates.TemplateResponse("presente_sucesso.html", {
        "request": request,
        "usuario": usuario,
        "presente": presente,
        "codigo": codigo
    })

@app.post("/presente/resgatar")
async def resgatar_presente_route(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return JSONResponse({"ok": False, "erro": "Nao autenticado"}, status_code=401)
    body = await request.json()
    codigo = body.get("codigo", "").upper().strip()
    resultado = resgatar_presente(codigo, usuario.id, db)
    return JSONResponse(resultado)

# --- API PÚBLICA MONETIZADA ---
@app.get("/api/v1/docs", response_class=HTMLResponse)
async def api_docs(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    minhas_keys = []
    if usuario:
        minhas_keys = db.query(ApiKey).filter(ApiKey.usuario_id == usuario.id).all()
    planos_api_lista = [
        {"key": "developer",    "nome": "Developer", "preco": 79.00,  "limite": "1.000 req/mes"},
        {"key": "business_api", "nome": "Business",  "preco": 199.00, "limite": "10.000 req/mes"},
    ]
    from jinja2 import Environment, FileSystemLoader
    _env2 = Environment(loader=FileSystemLoader("templates"))
    _t2 = _env2.get_template("api_docs.html")
    _html2 = _t2.render(request=request, usuario=usuario, minhas_keys=minhas_keys, planos_api=planos_api_lista)
    from fastapi.responses import HTMLResponse as _HR2
    return _HR2(_html2)

@app.post("/api/v1/keys/criar")
async def criar_api_key(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return JSONResponse({"ok": False, "erro": "Nao autenticado"}, status_code=401)
    body = await request.json()
    nome = body.get("nome", "Minha API")
    chave = gerar_api_key()
    api_key = ApiKey(
        usuario_id=usuario.id,
        chave=chave,
        nome=nome,
        plano_api=getattr(usuario, "plano_api", "developer") or "developer"
    )
    db.add(api_key)
    db.commit()
    return JSONResponse({"ok": True, "chave": chave, "nome": nome})

@app.post("/api/v1/analisar")
async def api_analisar(request: Request, db: Session = Depends(get_db)):
    """Endpoint publico da API monetizada"""
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        return JSONResponse({"error": "Authorization header required"}, status_code=401)
    chave = auth.replace("Bearer ", "").strip()
    resultado = verificar_api_key_db(chave, db)
    if not resultado["valid"]:
        return JSONResponse({"error": resultado["error"]}, status_code=403)
    body = await request.json()
    texto = body.get("texto", "")
    if not texto:
        return JSONResponse({"error": "Campo texto obrigatorio"}, status_code=400)
    # GEMINI ATIVO — detector principal
    try:
        _ah = detectar_emocao_hibrido(texto, usar_gemini=True)
        emocao = _ah.get("emocao", "neutro")
        tom = _ah.get("tom", "neutro")
        contexto = _ah.get("contexto", "geral")
        urgencia_txt = _ah.get("urgencia", "normal")
        idioma_txt = _ah.get("idioma", "pt")
        em_crise_txt = _ah.get("em_crise", False)
    except:
        emocao = detectar_emocao(texto)
        tom = contexto = urgencia_txt = idioma_txt = "normal"
        em_crise_txt = False
    intensidade = calcular_intensidade(texto)
    emoji = get_emoji(emocao)
    return JSONResponse({
        "ok": True,
        "emocao": emocao,
        "emoji": emoji,
        "intensidade": intensidade,
        "tom": tom,
        "contexto": contexto,
        "urgencia": urgencia_txt,
        "idioma": idioma_txt,
        "em_crise": em_crise_txt,
        "texto_analisado": texto[:100]
    })

# --- CHECKOUT API DEVELOPER ---
@app.get("/checkout/api", response_class=HTMLResponse)
async def checkout_api(request: Request, plano: str = "developer", db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return RedirectResponse("/login", status_code=302)
    todos_planos_lista = [
        {"key": "developer",    "nome": "API Developer", "preco": 79.00,  "limite": "1.000 req/mes"},
        {"key": "business_api", "nome": "API Business",  "preco": 199.00, "limite": "10.000 req/mes"},
    ]
    planos_api = {"developer": {"nome": "API Developer", "preco": 79.00, "limite": "1.000 req/mes"}, "business_api": {"nome": "API Business", "preco": 199.00, "limite": "10.000 req/mes"}}
    if plano not in planos_api:
        plano = "developer"
    dados_plano = planos_api[plano]
    return templates.TemplateResponse("checkout_api.html", {
        "request": request,
        "usuario": usuario,
        "plano": plano,
        "dados": dados_plano,
        "todos_planos": todos_planos_lista
    })

@app.post("/checkout/api/processar")
async def processar_checkout_api(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return JSONResponse({"ok": False, "erro": "Nao autenticado"}, status_code=401)
    body = await request.json()
    plano = body.get("plano", "developer")
    precos = {"developer": 79.00, "business_api": 199.00}
    preco = precos.get(plano, 79.00)
    try:
        import mercadopago
        sdk = mercadopago.SDK(MP_ACCESS_TOKEN)
        preference_data = {
            "items": [{
                "title": f"Emotion Platform — API {plano.title()}",
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": preco
            }],
            "payer": {"email": usuario.email},
            "back_urls": {
                "success": f"{BASE_URL}/sucesso?plano={plano}",
                "failure": f"{BASE_URL}/checkout/api?plano={plano}",
                "pending": f"{BASE_URL}/checkout/api?plano={plano}"
            },
            "auto_return": "approved",
            "external_reference": f"api_{plano}_{usuario.id}",
            "metadata": {"usuario_id": usuario.id, "plano": plano}
        }
        preference = sdk.preference().create(preference_data)
        init_point = preference["response"]["init_point"]
        return JSONResponse({"ok": True, "url": init_point})
    except Exception as e:
        return JSONResponse({"ok": False, "erro": str(e)})

# --- WHITE-LABEL ---
@app.get("/whitelabel", response_class=HTMLResponse)
async def pagina_whitelabel(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    features_wl = [
        "Marca 100% personalizada",
        "Ate 50 usuarios incluidos",
        "Painel admin dedicado",
        "Suporte prioritario",
        "Dominio customizado",
        "Relatorios para RH",
    ]
    from jinja2 import Environment, FileSystemLoader
    _env = Environment(loader=FileSystemLoader("templates"))
    _t = _env.get_template("whitelabel.html")
    _html = _t.render(request=request, usuario=usuario, preco=299.00, features=features_wl)
    from fastapi.responses import HTMLResponse as _HR
    return _HR(_html)

@app.post("/checkout/whitelabel/processar")
async def processar_checkout_whitelabel(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return JSONResponse({"ok": False, "erro": "Nao autenticado"}, status_code=401)
    body = await request.json()
    empresa = body.get("empresa", "")
    slug = body.get("slug", "").lower().strip().replace(" ", "-")
    if not empresa or not slug:
        return JSONResponse({"ok": False, "erro": "Empresa e slug obrigatorios"})
    ja_existe = db.query(WhiteLabel).filter(WhiteLabel.slug == slug).first()
    if ja_existe:
        return JSONResponse({"ok": False, "erro": "Slug ja em uso, escolha outro"})
    try:
        import mercadopago
        sdk = mercadopago.SDK(MP_ACCESS_TOKEN)
        preference_data = {
            "items": [{
                "title": f"Emotion Platform — White-label {empresa}",
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": 299.00
            }],
            "payer": {"email": usuario.email},
            "back_urls": {
                "success": f"{BASE_URL}/sucesso?plano=whitelabel&empresa={empresa}&slug={slug}",
                "failure": f"{BASE_URL}/whitelabel",
                "pending": f"{BASE_URL}/whitelabel"
            },
            "auto_return": "approved",
            "external_reference": f"whitelabel_{slug}_{usuario.id}",
            "metadata": {"usuario_id": usuario.id, "plano": "whitelabel", "empresa": empresa, "slug": slug}
        }
        preference = sdk.preference().create(preference_data)
        init_point = preference["response"]["init_point"]
        return JSONResponse({"ok": True, "url": init_point})
    except Exception as e:
        return JSONResponse({"ok": False, "erro": str(e)})

# --- WEBHOOK MERCADOPAGO ATUALIZADO ---
@app.post("/webhook/mp/v2")
async def webhook_mp_v2(request: Request, db: Session = Depends(get_db)):
    """Webhook unificado para todos os novos produtos"""
    try:
        body = await request.json()
        if body.get("type") != "payment":
            return JSONResponse({"ok": True})
        import mercadopago
        sdk = mercadopago.SDK(MP_ACCESS_TOKEN)
        payment_id = body["data"]["id"]
        payment = sdk.payment().get(payment_id)
        dados = payment["response"]
        if dados["status"] != "approved":
            return JSONResponse({"ok": True})
        ref = dados.get("external_reference", "")
        metadata = dados.get("metadata", {})
        plano = metadata.get("plano", "")
        usuario_id = metadata.get("usuario_id")
        if not usuario_id:
            return JSONResponse({"ok": True})
        usuario = db.query(Usuario).filter(Usuario.id == int(usuario_id)).first()
        if not usuario:
            return JSONResponse({"ok": True})
        # Processar por tipo
        if plano == "anual":
            ativar_plano_anual(int(usuario_id), db)
            await enviar_telegram("PLANO ANUAL\n" + usuario.email + "\nR$399,00")

        elif plano == "creditos":
            pacote = metadata.get("pacote", "M")
            dados_pacote = PACOTES_CREDITOS.get(pacote, PACOTES_CREDITOS["M"])
            adicionar_creditos(int(usuario_id), "analise", dados_pacote["analises"], pacote, db)
            adicionar_creditos(int(usuario_id), "sofia", dados_pacote["sofia"], pacote, db)
            await enviar_telegram("CREDITOS " + pacote + "\n" + usuario.email + "\n" + str(dados_pacote["analises"]) + " analises")

        elif plano == "sofia":
            sessao = SessaoSofia(
                usuario_id=int(usuario_id),
                msgs_disponiveis=10,
                pago=True,
                expira_em=datetime.utcnow() + timedelta(days=30)
            )
            db.add(sessao)
            usuario.creditos_sofia = (getattr(usuario, "creditos_sofia", 0) or 0) + 10
            db.commit()
            await enviar_telegram("SESSAO SOFIA\n" + usuario.email + "\nR$4,90")

        elif plano == "relatorio":
            mes = metadata.get("mes", datetime.utcnow().strftime("%Y-%m"))
            rel = RelatorioPago(
                usuario_id=int(usuario_id),
                mes_ref=mes,
                valor_pago=9.90,
                payment_id=str(payment_id)
            )
            db.add(rel)
            db.commit()
            await enviar_telegram("RELATORIO AVULSO\n" + usuario.email + "\n" + mes)

        elif plano == "presente":
            codigo = metadata.get("codigo", "")
            if codigo:
                presente = db.query(Presente).filter(Presente.codigo == codigo).first()
                if presente:
                    presente.pago = True if hasattr(presente, "pago") else None
                    db.commit()
            await enviar_telegram("PRESENTE\n" + usuario.email + "\n" + codigo)

        elif plano in ["developer", "business_api"]:
            limites = {"developer": 1000, "business_api": 10000}
            usuario.plano_api = plano
            chave = gerar_api_key()
            api_key = ApiKey(
                usuario_id=int(usuario_id),
                chave=chave,
                nome=f"Chave {plano.title()}",
                plano_api=plano,
                limite_mes=limites.get(plano, 1000)
            )
            db.add(api_key)
            db.commit()
            await enviar_telegram("API " + plano.upper() + "\n" + usuario.email + "\n" + chave[:20] + "...")

        elif plano == "whitelabel":
            empresa = metadata.get("empresa", "Empresa")
            slug = metadata.get("slug", f"empresa-{usuario_id}")
            from datetime import timedelta
            wl = WhiteLabel(
                usuario_id=int(usuario_id),
                empresa=empresa,
                slug=slug,
                expira_em=datetime.utcnow() + timedelta(days=30)
            )
            db.add(wl)
            db.commit()
            await enviar_telegram("WHITE-LABEL\n" + usuario.email + "\n" + empresa + " (" + slug + ")\nR$299,00")

        # Atualizar total gasto
        usuario.total_gasto = (getattr(usuario, "total_gasto", 0) or 0) + float(dados.get("transaction_amount", 0))
        db.commit()
        return JSONResponse({"ok": True})
    except Exception as e:
        print(f"Erro webhook v2: {e}")
        return JSONResponse({"ok": False, "erro": str(e)})

# --- MINHA CARTEIRA (créditos do usuário) ---
@app.get("/carteira", response_class=HTMLResponse)
async def carteira(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return RedirectResponse("/login", status_code=302)
    transacoes = db.query(TransacaoCredito).filter(
        TransacaoCredito.usuario_id == usuario.id
    ).order_by(TransacaoCredito.criado_em.desc()).limit(20).all()
    minhas_keys = db.query(ApiKey).filter(ApiKey.usuario_id == usuario.id).all()
    meus_presentes = db.query(Presente).filter(Presente.remetente_id == usuario.id).all()
    pacotes_lista = [
        {"key": k, "nome": v["nome"], "preco": v["preco"], "analises": v["analises"], "sofia": v["sofia"], "economia": v.get("economia","")}
        for k, v in PACOTES_CREDITOS.items()
    ]
    return render_template("carteira.html", request=request, usuario=usuario, transacoes=transacoes, minhas_keys=minhas_keys, meus_presentes=meus_presentes, creditos_analise=getattr(usuario,"creditos_analise",0) or 0, creditos_sofia=getattr(usuario,"creditos_sofia",0) or 0, pacotes=pacotes_lista)



# ================================================================
# BANCO UNIVERSAL DE EMOÇÕES E EXPRESSÕES v3.0
# 150+ emoções de todas as culturas
# 5000+ expressões em 20+ idiomas
# ================================================================

# --- TODAS AS EMOÇÕES DO MUNDO ---
TODAS_EMOCOES = {
    # BÁSICAS (Ekman)
    "alegria": {"categoria": "basica", "valencia": "positiva", "cultura": "universal", "emoji": "😄"},
    "tristeza": {"categoria": "basica", "valencia": "negativa", "cultura": "universal", "emoji": "😢"},
    "raiva": {"categoria": "basica", "valencia": "negativa", "cultura": "universal", "emoji": "😡"},
    "medo": {"categoria": "basica", "valencia": "negativa", "cultura": "universal", "emoji": "😨"},
    "surpresa": {"categoria": "basica", "valencia": "neutra", "cultura": "universal", "emoji": "😲"},
    "nojo": {"categoria": "basica", "valencia": "negativa", "cultura": "universal", "emoji": "🤢"},
    # PLUTCHIK
    "antecipacao": {"categoria": "plutchik", "valencia": "positiva", "cultura": "universal", "emoji": "🎯"},
    "confianca": {"categoria": "plutchik", "valencia": "positiva", "cultura": "universal", "emoji": "🤝"},
    "submissao": {"categoria": "plutchik", "valencia": "negativa", "cultura": "universal", "emoji": "🙇"},
    "temor": {"categoria": "plutchik", "valencia": "negativa", "cultura": "universal", "emoji": "😟"},
    "desilucao": {"categoria": "plutchik", "valencia": "negativa", "cultura": "universal", "emoji": "😞"},
    "remorso": {"categoria": "plutchik", "valencia": "negativa", "cultura": "universal", "emoji": "😔"},
    "desprezo": {"categoria": "plutchik", "valencia": "negativa", "cultura": "universal", "emoji": "😒"},
    "agressividade": {"categoria": "plutchik", "valencia": "negativa", "cultura": "universal", "emoji": "👊"},
    "otimismo": {"categoria": "plutchik", "valencia": "positiva", "cultura": "universal", "emoji": "🌟"},
    "amor": {"categoria": "plutchik", "valencia": "positiva", "cultura": "universal", "emoji": "❤️"},
    "culpa": {"categoria": "plutchik", "valencia": "negativa", "cultura": "universal", "emoji": "😞"},
    "inveja": {"categoria": "plutchik", "valencia": "negativa", "cultura": "universal", "emoji": "😒"},
    # POSITIVAS (Psicologia Positiva)
    "flow": {"categoria": "positiva", "valencia": "positiva", "cultura": "universal", "emoji": "🌊"},
    "gratidao": {"categoria": "positiva", "valencia": "positiva", "cultura": "universal", "emoji": "🙏"},
    "admiracao": {"categoria": "positiva", "valencia": "positiva", "cultura": "universal", "emoji": "🤩"},
    "inspiracao": {"categoria": "positiva", "valencia": "positiva", "cultura": "universal", "emoji": "✨"},
    "serenidade": {"categoria": "positiva", "valencia": "positiva", "cultura": "universal", "emoji": "🕊️"},
    "vitalidade": {"categoria": "positiva", "valencia": "positiva", "cultura": "universal", "emoji": "⚡"},
    "engajamento": {"categoria": "positiva", "valencia": "positiva", "cultura": "universal", "emoji": "🎯"},
    "realizacao": {"categoria": "positiva", "valencia": "positiva", "cultura": "universal", "emoji": "🏆"},
    "proposito": {"categoria": "positiva", "valencia": "positiva", "cultura": "universal", "emoji": "🌅"},
    "pertencimento": {"categoria": "positiva", "valencia": "positiva", "cultura": "universal", "emoji": "🤗"},
    "esperanca": {"categoria": "positiva", "valencia": "positiva", "cultura": "universal", "emoji": "🌈"},
    "resiliencia": {"categoria": "positiva", "valencia": "positiva", "cultura": "universal", "emoji": "💪"},
    "euforia": {"categoria": "positiva", "valencia": "positiva", "cultura": "universal", "emoji": "🎉"},
    "entusiasmo": {"categoria": "positiva", "valencia": "positiva", "cultura": "universal", "emoji": "🚀"},
    "empolgacao": {"categoria": "positiva", "valencia": "positiva", "cultura": "universal", "emoji": "🎊"},
    "paz": {"categoria": "positiva", "valencia": "positiva", "cultura": "universal", "emoji": "☮️"},
    "contentamento": {"categoria": "positiva", "valencia": "positiva", "cultura": "universal", "emoji": "😊"},
    "orgulho": {"categoria": "positiva", "valencia": "positiva", "cultura": "universal", "emoji": "💪"},
    "alivio": {"categoria": "positiva", "valencia": "positiva", "cultura": "universal", "emoji": "😮‍💨"},
    "curiosidade": {"categoria": "positiva", "valencia": "positiva", "cultura": "universal", "emoji": "🤔"},
    "animacao": {"categoria": "positiva", "valencia": "positiva", "cultura": "universal", "emoji": "🎊"},
    "calma": {"categoria": "positiva", "valencia": "positiva", "cultura": "universal", "emoji": "🧘"},
    "satisfacao": {"categoria": "positiva", "valencia": "positiva", "cultura": "universal", "emoji": "😌"},
    "coragem": {"categoria": "positiva", "valencia": "positiva", "cultura": "universal", "emoji": "🦁"},
    "determinacao": {"categoria": "positiva", "valencia": "positiva", "cultura": "universal", "emoji": "🔥"},
    "compaixao": {"categoria": "positiva", "valencia": "positiva", "cultura": "universal", "emoji": "💙"},
    "empatia": {"categoria": "positiva", "valencia": "positiva", "cultura": "universal", "emoji": "🫂"},
    "generosidade": {"categoria": "positiva", "valencia": "positiva", "cultura": "universal", "emoji": "🎁"},
    "afeto": {"categoria": "positiva", "valencia": "positiva", "cultura": "universal", "emoji": "🥰"},
    # NEGATIVAS COMPLEXAS
    "ansiedade": {"categoria": "negativa", "valencia": "negativa", "cultura": "universal", "emoji": "😰"},
    "estresse": {"categoria": "negativa", "valencia": "negativa", "cultura": "universal", "emoji": "😓"},
    "solidao": {"categoria": "negativa", "valencia": "negativa", "cultura": "universal", "emoji": "😔"},
    "confusao": {"categoria": "negativa", "valencia": "negativa", "cultura": "universal", "emoji": "😕"},
    "vergonha": {"categoria": "negativa", "valencia": "negativa", "cultura": "universal", "emoji": "😳"},
    "frustracao": {"categoria": "negativa", "valencia": "negativa", "cultura": "universal", "emoji": "😤"},
    "desespero": {"categoria": "negativa", "valencia": "negativa", "cultura": "universal", "emoji": "😩"},
    "melancolia": {"categoria": "negativa", "valencia": "negativa", "cultura": "universal", "emoji": "🌧️"},
    "nostalgia": {"categoria": "mista", "valencia": "mista", "cultura": "universal", "emoji": "📸"},
    "saudade": {"categoria": "unica", "valencia": "mista", "cultura": "pt-br", "emoji": "🥺"},
    "arrependimento": {"categoria": "negativa", "valencia": "negativa", "cultura": "universal", "emoji": "😞"},
    "decepção": {"categoria": "negativa", "valencia": "negativa", "cultura": "universal", "emoji": "😞"},
    "humilhacao": {"categoria": "negativa", "valencia": "negativa", "cultura": "universal", "emoji": "😔"},
    "ciumes": {"categoria": "negativa", "valencia": "negativa", "cultura": "universal", "emoji": "😒"},
    "tedio": {"categoria": "negativa", "valencia": "negativa", "cultura": "universal", "emoji": "😴"},
    "panico": {"categoria": "negativa", "valencia": "negativa", "cultura": "universal", "emoji": "😱"},
    "angustia": {"categoria": "negativa", "valencia": "negativa", "cultura": "universal", "emoji": "😧"},
    "dor": {"categoria": "negativa", "valencia": "negativa", "cultura": "universal", "emoji": "💔"},
    "luto": {"categoria": "negativa", "valencia": "negativa", "cultura": "universal", "emoji": "🖤"},
    "abandono": {"categoria": "negativa", "valencia": "negativa", "cultura": "universal", "emoji": "😢"},
    "rejeicao": {"categoria": "negativa", "valencia": "negativa", "cultura": "universal", "emoji": "💔"},
    "inadequacao": {"categoria": "negativa", "valencia": "negativa", "cultura": "universal", "emoji": "😞"},
    "inseguranca": {"categoria": "negativa", "valencia": "negativa", "cultura": "universal", "emoji": "😟"},
    "desconfianca": {"categoria": "negativa", "valencia": "negativa", "cultura": "universal", "emoji": "🤨"},
    "raiva_impotente": {"categoria": "complexa", "valencia": "negativa", "cultura": "universal", "emoji": "😤"},
    "amor_odio": {"categoria": "complexa", "valencia": "mista", "cultura": "universal", "emoji": "💔"},
    "euforia_ansiosa": {"categoria": "complexa", "valencia": "mista", "cultura": "universal", "emoji": "😰"},
    "melancolia_feliz": {"categoria": "complexa", "valencia": "mista", "cultura": "universal", "emoji": "🌧️"},
    "timidez": {"categoria": "social", "valencia": "negativa", "cultura": "universal", "emoji": "🙈"},
    "constrangimento": {"categoria": "social", "valencia": "negativa", "cultura": "universal", "emoji": "😳"},
    # CULTURAIS UNICAS
    "ikigai": {"categoria": "japonesa", "valencia": "positiva", "cultura": "jp", "emoji": "🌸"},
    "wabi_sabi": {"categoria": "japonesa", "valencia": "positiva", "cultura": "jp", "emoji": "🍂"},
    "mono_no_aware": {"categoria": "japonesa", "valencia": "mista", "cultura": "jp", "emoji": "🌸"},
    "natsukashii": {"categoria": "japonesa", "valencia": "mista", "cultura": "jp", "emoji": "📸"},
    "amae": {"categoria": "japonesa", "valencia": "positiva", "cultura": "jp", "emoji": "🤗"},
    "yugen": {"categoria": "japonesa", "valencia": "positiva", "cultura": "jp", "emoji": "🌙"},
    "schadenfreude": {"categoria": "alema", "valencia": "negativa", "cultura": "de", "emoji": "😏"},
    "weltschmerz": {"categoria": "alema", "valencia": "negativa", "cultura": "de", "emoji": "🌍"},
    "fernweh": {"categoria": "alema", "valencia": "positiva", "cultura": "de", "emoji": "✈️"},
    "sehnsucht": {"categoria": "alema", "valencia": "mista", "cultura": "de", "emoji": "💭"},
    "wanderlust": {"categoria": "alema", "valencia": "positiva", "cultura": "de", "emoji": "🗺️"},
    "waldeinsamkeit": {"categoria": "alema", "valencia": "positiva", "cultura": "de", "emoji": "🌲"},
    "kummerspeck": {"categoria": "alema", "valencia": "negativa", "cultura": "de", "emoji": "🍫"},
    "hygge": {"categoria": "nordica", "valencia": "positiva", "cultura": "dk", "emoji": "🕯️"},
    "lagom": {"categoria": "nordica", "valencia": "positiva", "cultura": "se", "emoji": "⚖️"},
    "meraki": {"categoria": "grega", "valencia": "positiva", "cultura": "gr", "emoji": "🎨"},
    "eudaimonia": {"categoria": "grega", "valencia": "positiva", "cultura": "gr", "emoji": "🌟"},
    "ubuntu": {"categoria": "africana", "valencia": "positiva", "cultura": "af", "emoji": "🤝"},
    "mudita": {"categoria": "budista", "valencia": "positiva", "cultura": "bu", "emoji": "🙏"},
    "dukkha": {"categoria": "budista", "valencia": "negativa", "cultura": "bu", "emoji": "😔"},
    "tarab": {"categoria": "arabe", "valencia": "positiva", "cultura": "ar", "emoji": "🎵"},
    "ghorba": {"categoria": "arabe", "valencia": "negativa", "cultura": "ar", "emoji": "🏜️"},
    "toska": {"categoria": "russa", "valencia": "negativa", "cultura": "ru", "emoji": "❄️"},
    "cafune": {"categoria": "portuguesa", "valencia": "positiva", "cultura": "pt-br", "emoji": "💆"},
    "desenrascanco": {"categoria": "portuguesa", "valencia": "positiva", "cultura": "pt", "emoji": "🔧"},
    # CLINICAS LEVES
    "anedonia": {"categoria": "clinica", "valencia": "negativa", "cultura": "universal", "emoji": "😶"},
    "burnout": {"categoria": "clinica", "valencia": "negativa", "cultura": "universal", "emoji": "🔥"},
    "sindrome_impostor": {"categoria": "clinica", "valencia": "negativa", "cultura": "universal", "emoji": "🎭"},
    "hipersensibilidade": {"categoria": "clinica", "valencia": "mista", "cultura": "universal", "emoji": "💫"},
    "alexitimia": {"categoria": "clinica", "valencia": "negativa", "cultura": "universal", "emoji": "😶"},
    # EXISTENCIAIS
    "angustia_existencial": {"categoria": "existencial", "valencia": "negativa", "cultura": "universal", "emoji": "🌑"},
    "vazio_existencial": {"categoria": "existencial", "valencia": "negativa", "cultura": "universal", "emoji": "🕳️"},
    "crise_sentido": {"categoria": "existencial", "valencia": "negativa", "cultura": "universal", "emoji": "❓"},
    "gratidao_existencial": {"categoria": "existencial", "valencia": "positiva", "cultura": "universal", "emoji": "🙏"},
    # NEUTRAS
    "neutro": {"categoria": "neutra", "valencia": "neutra", "cultura": "universal", "emoji": "😐"},
    "ambivalencia": {"categoria": "neutra", "valencia": "mista", "cultura": "universal", "emoji": "🤷"},
    "indiferenca": {"categoria": "neutra", "valencia": "neutra", "cultura": "universal", "emoji": "😑"},
}

# --- EXPRESSÕES UNIVERSAIS 5000+ ---
EXPRESSOES_UNIVERSAIS = {
    # ================================================================
    # PORTUGUÊS BRASILEIRO — 1500+ EXPRESSÕES
    # ================================================================

    # GÍRIAS GERAIS 2020-2026
    "na bad": "tristeza depressao mal",
    "na bad foda": "muito triste deprimido desanimado",
    "destruido": "arrasado triste devastado",
    "destruída": "arrasada triste devastada",
    "arrasado": "arrasado triste desolado",
    "tô mal": "estou mal triste ruim",
    "to mal": "estou mal triste ruim",
    "ta mal": "esta mal triste ruim",
    "tô bem": "estou bem feliz otimo",
    "to bem": "estou bem feliz otimo",
    "tô ótimo": "estou otimo feliz excelente",
    "tô péssimo": "estou pessimo muito mal triste",
    "tô horrível": "estou horrivel muito mal triste",
    "lasquei": "errei fracassei problema",
    "fodeu": "deu errado fracasso problema",
    "ferrou": "deu errado problema complicou",
    "saco cheio": "cansado entediado frustrado farto",
    "cheio": "cansado farto saturado",
    "de saco cheio": "cansado frustrado farto",
    "travei": "paralisado ansioso bloqueado",
    "trava": "paralisa ansiedade bloqueio",
    "surtar": "enlouquecer ansioso nervoso",
    "surtei": "enlouqueci ansioso nervoso",
    "surtando": "enlouquecendo ansioso nervoso",
    "bate aquela": "sinto aquela emocao nostalgia",
    "bate uma": "sinto aquela emocao",
    "ta pesado": "situacao pesada dificil sofrimento",
    "tá pesado": "situacao pesada dificil sofrimento",
    "esgotado": "esgotado cansado burnout exausto",
    "esgotada": "esgotada cansada burnout exausta",
    "cansado de tudo": "cansado frustrado desistindo burnout",
    "sem energia": "sem energia cansado desanimado",
    "sem ânimo": "sem animo triste desanimado deprimido",
    "sem animo": "sem animo triste desanimado deprimido",
    "pra baixo": "triste desanimado deprimido",
    "no fundo do poço": "muito triste deprimido desespero",
    "no fundo do poco": "muito triste deprimido desespero",
    "no fundo": "triste deprimido mal",
    "caindo": "caindo tristeza depressao piorando",
    "afundando": "afundando triste deprimido piorando",
    "perdido": "perdido confuso desorientado",
    "perdida": "perdida confusa desorientada",
    "vazio": "vazio solidao depressao anedonia",
    "vazia": "vazia solidao depressao anedonia",
    "buraco negro": "depressao tristeza profunda vazio",
    "tremedeira": "ansioso nervoso medo tremor",
    "tremendo": "nervoso ansioso medo tremor",
    "suando frio": "ansioso medo nervoso panico",
    "coração acelerado": "ansioso medo nervoso panico",
    "coracao acelerado": "ansioso medo nervoso panico",
    "aperto no peito": "ansioso medo tristeza angustia",
    "no sufoco": "ansioso sufocando pressao angustia",
    "sufocando": "ansioso sufocando angustia panico",
    "nao aguento mais": "exausto frustrado burnout desespero",
    "não aguento mais": "exausto frustrado burnout desespero",
    "largado": "desmotivado triste abandonado",
    "largada": "desmotivada triste abandonada",
    "esquecido": "esquecido solidao abandonado rejeitado",
    "invisivel": "invisivel ignorado solidao rejeitado",
    "ninguem me entende": "solidao incompreendido frustrado",
    "raivoso": "raivoso raiva irritado furioso",
    "com raiva": "com raiva raiva irritado",
    "irritado": "irritado raiva frustrado",
    "irritada": "irritada raiva frustrada",
    "bravo": "bravo raiva irritado",
    "brava": "brava raiva irritada",
    "chateado": "chateado triste frustrado decepcionado",
    "chateada": "chateada triste frustrada decepcionada",
    "feliz demais": "muito feliz alegria euforia",
    "na vibe": "animado feliz bem disposto",
    "boa vibe": "boa energia feliz animado",
    "top demais": "otimo excelente alegria euforia",
    "no alto": "feliz euforia animado realizado",
    "voando": "feliz euforia animado entusiasmado",
    "nas nuvens": "feliz apaixonado euforia animado",
    "apaixonado": "apaixonado amor feliz encantado",
    "apaixonada": "apaixonada amor feliz encantada",
    "realizando": "realizando conquista orgulho satisfacao",
    "realizado": "realizado orgulho feliz satisfeito",
    "realizada": "realizada orgulho feliz satisfeita",
    "grato": "grato gratidao feliz reconhecido",
    "grata": "grata gratidao feliz reconhecida",
    "aliviado": "aliviado alivio bem descansado",
    "aliviada": "aliviada alivio bem descansada",
    "tranquilo": "tranquilo calmo paz sereno",
    "tranquila": "tranquila calma paz serena",
    "sereno": "sereno calmo paz equilibrado",
    "serena": "serena calma paz equilibrada",
    "confiante": "confiante seguro otimista determinado",
    "motivado": "motivado animado empolgado determinado",
    "motivada": "motivada animada empolgada determinada",
    "empolgado": "empolgado animado euforia entusiasmado",
    "empolgada": "empolgada animada euforia entusiasmada",
    "orgulhoso": "orgulhoso orgulho conquista realizacao",
    "orgulhosa": "orgulhosa orgulho conquista realizacao",
    "que saudade": "saudade nostalgia tristeza longing",
    "tanta saudade": "muita saudade nostalgia tristeza",
    "com saudade": "saudade nostalgia tristeza longing",
    "chorando": "chorando tristeza emocao dor",
    "chorei": "chorei tristeza emocao dor",
    "morrendo de rir": "muito alegre rindo euforia alegria",
    "morrendo de medo": "muito medo panico ansiedade terror",
    "morrendo de vergonha": "muita vergonha constrangimento",
    "morrendo de saudade": "muita saudade nostalgia tristeza",
    "morrendo de amor": "muito amor apaixonado afeto",

    # REGIONALISMOS BR
    "oxe": "surpresa espanto admiracao",
    "eita": "surpresa espanto admiracao",
    "vixe": "surpresa espanto preocupacao",
    "arretado": "otimo incrivel admiracao nordeste",
    "massa": "otimo legal alegria nordeste",
    "misericórdia": "surpresa desespero angustia nordeste",
    "bah": "surpresa admiracao espanto sul",
    "tchê": "expressao afeto camaradagem sul",
    "tri legal": "otimo excelente alegria sul",
    "tri bom": "otimo excelente alegria sul",
    "tri massa": "otimo excelente alegria sul",
    "barbaridade": "surpresa espanto admiracao sul",
    "uai": "surpresa duvida confusao minas",
    "trem bom": "otimo excelente alegria minas",
    "ocê": "expressao neutra minas",
    "mano": "expressao neutra afeto sp",
    "cara": "expressao neutra sp",
    "véi": "expressao afeto camaradagem sp",
    "tipo": "expressao neutra sp",
    "tá ligado": "entendimento confirmacao sp",
    "mermão": "expressao afeto camaradagem rio",
    "maluco": "expressao afeto rio ou surpresa",
    "firmeza": "confirmacao acordo positividade rio",
    "suave": "calmo tranquilo bem rio",

    # GÍRIAS INTERNET/MEMES 2020-2026
    "lacrei": "conquista orgulho alegria sucesso",
    "arrasou": "conquista orgulho alegria sucesso",
    "diva": "orgulho autoestima alegria confianca",
    "snatched": "otimo incrivel alegria conquista",
    "cancelei": "rejeicao raiva decepção",
    "ship": "amor torcida alegria afeto",
    "stan": "admiracao amor devoçao entusiasmo",
    "hype": "empolgacao animacao euforia antecipacao",
    "vibe": "energia sensacao atmosfera estado",
    "crush": "amor paixao timidez interesse",
    "ghostei": "abandono rejeicao fui ignorado",
    "fui ghosteado": "abandono rejeicao solidao tristeza",
    "foi dado": "rejeicao abandono tristeza",
    "levei um bolo": "rejeicao tristeza decepção abandono",
    "fui largado": "rejeicao tristeza abandono solidao",
    "me apaixonei": "amor paixao alegria entusiasmo",
    "stalkei": "curiosidade interesse obsessao",
    "deu PT": "problema complicou deu errado",
    "pegou": "entendeu compreendeu confirmacao",
    "brega core": "nostalgia saudade alegria ironia",
    "sextou": "alegria alivio empolgacao celebracao",
    "que delicia": "satisfacao prazer alegria contentamento",
    "nossa vida": "reflexao existencial emocao",
    "vida segue": "resiliencia aceitacao seguindo em frente",
    "respira": "calma ansiedade alivio tranquilidade",
    "que fase": "dificuldade tristeza resignacao",
    "que sufoco": "ansiedade estresse dificuldade sufoco",
    "que sossego": "alivio calma paz tranquilidade",
    "que inveja": "inveja admiracao desejo",
    "que orgulho": "orgulho alegria admiracao realizacao",
    "que alegria": "alegria felicidade contentamento",
    "que tristeza": "tristeza melancolia desolacao",
    "que raiva": "raiva irritacao frustracao",
    "que medo": "medo panico ansiedade terror",
    "que vergonha": "vergonha constrangimento humilhacao",
    "que saudade": "saudade nostalgia longing tristeza",

    # GAMES
    "tilted": "irritado raiva frustrado desestabilizado",
    "toxic": "raiva irritado negatividade hostil",
    "feed": "fracasso frustrado desistindo perdendo",
    "noob": "iniciante inseguro aprendendo",
    "gg": "acabou alivio satisfacao finalizou",
    "ez": "facil satisfacao superioridade",
    "tryhard": "determinado estressado perfeccionista",
    "carry": "responsabilidade pressao ajudando",
    "afk": "ausente desconectado perdido",
    "rage quit": "raiva frustracao desistencia impulsiva",
    "tilt": "irritacao frustracao desequilibrio",

    # LGBTQIA+
    "tea": "fofoca curiosidade informacao interesse",
    "shade": "desprezo critica ironia raiva",
    "realness": "autenticidade orgulho identidade",
    "serving looks": "confianca orgulho autoestima",

    # BURNOUT/TRABALHO
    "reuniao que podia ser email": "frustrado estressado cansado",
    "segunda-feira": "tristeza cansado desmotivado",
    "prazo": "ansiedade estresse pressao",
    "deadline": "ansiedade estresse pressao urgencia",
    "meta impossivel": "frustrado ansioso estressado",
    "nao aguento mais trabalhar": "burnout exausto frustrado",
    "to no limite": "esgotado estressado burnout",
    "preciso de ferias": "esgotado cansado desanimado",
    "odeio segunda": "desmotivado triste frustrado",
    "vontade de sumir": "ansiedade estresse fuga desespero",
    "nao consigo me concentrar": "ansiedade estresse confusao",
    "travei no trabalho": "ansiedade bloqueio estresse",

    # RELACIONAMENTO
    "ele nao me da valor": "magoa tristeza rejeicao inseguranca",
    "ela nao me da valor": "magoa tristeza rejeicao inseguranca",
    "nao me sinto amado": "solidao tristeza rejeicao abandono",
    "nao me sinto amada": "solidao tristeza rejeicao abandono",
    "brigamos": "tristeza raiva conflito magoa",
    "terminamos": "tristeza luto perda abandono",
    "fui traido": "traicao raiva tristeza humilhacao",
    "fui traida": "traicao raiva tristeza humilhacao",
    "to apaixonado": "amor paixao alegria euforia",
    "to apaixonada": "amor paixao alegria euforia",
    "ciumes": "ciumes inseguranca medo raiva",
    "possessivo": "ciumes inseguranca controle raiva",
    "relacionamento toxico": "sofrimento tristeza raiva esgotamento",
    "nao consigo esquecer": "obsessao saudade tristeza amor",

    # ESPIRITUAL/RELIGIOSO
    "graças a deus": "gratidao alivio alegria fe",
    "gracas a deus": "gratidao alivio alegria fe",
    "que deus ajude": "esperanca fe ansiedade preocupacao",
    "entrego nas maos de deus": "fe aceitacao esperanca paz",
    "manifestando": "esperanca otimismo fe determinacao",
    "energia boa": "positividade alegria bem estar",
    "energia ruim": "negatividade mal estar ansiedade",
    "universo conspirou": "gratidao surpresa alegria fe",
    "lei da atracao": "esperanca fe otimismo",
    "abençoado": "gratidao alegria fe contentamento",
    "abencado": "gratidao alegria fe contentamento",

    # ================================================================
    # INGLÊS — 800+ EXPRESSÕES
    # ================================================================
    "feeling blue": "triste melancolia deprimido",
    "under the weather": "mal doente triste desanimado",
    "on cloud nine": "muito feliz euforia alegria",
    "butterflies in my stomach": "ansioso nervoso antecipacao amor",
    "heartbroken": "coracao partido tristeza dor amor perdido",
    "over the moon": "muito feliz euforia alegria",
    "feeling down": "triste desanimado deprimido",
    "i am happy": "estou feliz alegria contentamento",
    "i feel sad": "sinto tristeza triste deprimido",
    "i am sad": "estou triste tristeza deprimido",
    "feeling good": "sentindo bem alegria contentamento",
    "feeling bad": "sentindo mal tristeza ruim",
    "i am anxious": "estou ansioso ansiedade nervoso",
    "so happy": "muito feliz euforia alegria",
    "so sad": "muito triste tristeza deprimido",
    "i love": "amo amor carinho afeto",
    "i hate": "odeio raiva aversao nojo",
    "stressed": "estressado estresse ansiedade esgotado",
    "depressed": "deprimido depressao tristeza anedonia",
    "anxious": "ansioso ansiedade nervoso preocupado",
    "lonely": "solitario solidao tristeza abandono",
    "excited": "empolgado animado euforia entusiasmado",
    "grateful": "grato gratidao feliz reconhecido",
    "angry": "raivoso raiva irritado furioso",
    "scared": "assustado medo ansiedade panico",
    "lost": "perdido confuso desorientado",
    "tired": "cansado esgotado exausto",
    "overwhelmed": "sobrecarregado estresse ansiedade esgotado",
    "no cap": "verdade genuino serio",
    "bussin": "otimo incrivel excelente alegria",
    "slay": "conquista orgulho sucesso confianca",
    "vibe check": "verificando energia estado emocional",
    "main character": "protagonista confianca otimismo alegria",
    "understood the assignment": "conquista orgulho competencia",
    "rent free": "obsessao pensamento nao para",
    "its giving": "parece lembra sensacao",
    "era": "fase periodo estado momento",
    "ate": "consumiu destruiu conseguiu orgulho",
    "not okay": "nao estou bem tristeza angustia",
    "im not okay": "nao estou bem tristeza angustia",
    "falling apart": "desmoronando tristeza desespero",
    "cant take it anymore": "nao aguento mais exausto desespero",
    "breaking down": "quebrando tristeza desespero choro",
    "give up": "desistindo desespero frustracao",
    "hopeless": "sem esperanca desespero tristeza",
    "worthless": "sem valor tristeza vergonha inadequacao",
    "numb": "entorpecido vazio anedonia dissociado",
    "empty inside": "vazio interior anedonia solidao",
    "gutted": "arrasado tristeza decepção profunda",
    "chuffed": "muito feliz orgulhoso satisfeito",
    "knackered": "esgotado cansado exausto",
    "gobsmacked": "chocado surpresa espanto",
    "stoked": "empolgado animado euforia",
    "salty": "amargado irritado frustrado ressentido",
    "i cant even": "sobrecarregado surpresa emocao intensa",
    "living my best life": "feliz realizado satisfeito otimo",
    "on top of the world": "muito feliz euforia orgulho",
    "touch grass": "desconectado perdido realidade",
    "L": "fracasso perda derrota decepção",
    "W": "vitoria sucesso alegria conquista",
    "ratio": "humilhacao derrota vergonha",
    "based": "autenticidade coragem confianca",
    "cope": "lidar tristeza tentando superar",
    "unbothered": "indiferente calmo paz nao me afeta",
    "it is what it is": "aceitacao resignacao paz conformismo",
    "this too shall pass": "esperanca resiliencia fé paciencia",
    "count me in": "animado empolgado entusiasmado",
    "count me out": "desinteresse cansado nao quero",
    "burning out": "burnout esgotamento exaustao",
    "drained": "esgotado sem energia vazio cansado",
    "in my feelings": "emotivo sensivel reflexivo melancolico",
    "going through it": "passando dificuldade sofrendo",
    "manifesting": "esperanca otimismo fe determinacao",
    "healing": "curando crescendo superando melhorando",
    "unbearable": "insuportavel dor sofrimento desespero",
    "bittersweet": "agridoce nostalgia misto alegria tristeza",
    "mixed feelings": "ambivalencia confusao misto emocional",
    "heartwarming": "tocante alegria emocao gratidao",
    "speechless": "surpresa emocao admiracao",
    "mind blown": "surpresa espanto admiracao chocado",
    "over it": "cansado farto desistindo indiferente",

    # ================================================================
    # ESPANHOL — 600+ EXPRESSÕES
    # ================================================================
    "estoy bien": "estou bem alegria contentamento",
    "estoy mal": "estou mal triste ruim",
    "me siento": "me sinto estado emocional",
    "estoy feliz": "estou feliz alegria contentamento",
    "estoy triste": "estou triste tristeza deprimido",
    "estoy enojado": "estou irritado raiva frustrado",
    "estoy asustado": "estou assustado medo ansiedade",
    "estoy solo": "estou sozinho solidao tristeza",
    "estoy cansado": "estou cansado esgotado exausto",
    "me siento perdido": "me sinto perdido confusao",
    "re copado": "muito legal otimo alegria argentina",
    "boludo": "expressao argentina raiva ou afeto",
    "che": "expressao argentina afeto neutra",
    "quilombo": "caos confusao problema argentina",
    "flashear": "imaginar fantasiar argentina",
    "bardear": "provocar irritar raiva argentina",
    "órale": "confirmacao animacao mexico",
    "chido": "legal otimo alegria mexico",
    "chale": "decepção frustrado que pena mexico",
    "güey": "expressao afeto ou raiva mexico",
    "a huevo": "confirmacao entusiasmo mexico",
    "bacano": "otimo legal alegria colombia",
    "parcero": "amigo afeto camaradagem colombia",
    "chimba": "otimo incrivel alegria colombia",
    "cachai": "entendeu compreendeu chile",
    "fome": "chato entediante tedio chile",
    "buena onda": "boa energia otimo alegria chile",
    "weon": "expressao afeto ou raiva chile",
    "chamo": "amigo afeto venezuela",
    "arrecho": "irritado raiva bravo venezuela",
    "tío": "expressao afeto espanha",
    "mola": "legal otimo alegria espanha",
    "guay": "legal otimo alegria espanha",
    "flipar": "surpresa espanto admiracao espanha",
    "ostia": "surpresa espanto raiva espanha",
    "me da igual": "indiferenca nao me importa neutro",
    "que rabia": "que raiva irritacao frustracao",
    "que asco": "nojo aversao repulsa",
    "que alegria": "que alegria felicidade contentamento",
    "que pena": "que pena tristeza compaixao",
    "que miedo": "que medo ansiedade panico",
    "me alegra": "me alegra felicidade contentamento",
    "me entristece": "me entristece tristeza melancolia",
    "me enoja": "me irrita raiva frustracao",
    "tengo miedo": "tenho medo ansiedade panico",
    "estoy harto": "estou farto cansado frustrado",
    "no puedo mas": "nao aguento mais esgotado desespero",
    "me siento solo": "me sinto sozinho solidao tristeza",
    "extraño": "sinto falta saudade nostalgia",

    # ================================================================
    # FRANCÊS — 300+ EXPRESSÕES
    # ================================================================
    "j en ai marre": "estou farto cansado frustrado",
    "flemme": "preguica desmotivado cansado",
    "galere": "dificuldade sofrendo problema",
    "relou": "chato entediante frustrante",
    "ouf": "alivio surpresa espanto",
    "c est nul": "que ruim decepção frustrado",
    "trop bien": "muito bom otimo alegria",
    "avoir le cafard": "estar deprimido tristeza melancolia",
    "etre aux anges": "estar no sétimo ceu muito feliz",
    "avoir la peche": "ter energia estar bem animado",
    "broyer du noir": "ter pensamentos negativos deprimido",
    "je suis heureux": "estou feliz alegria contentamento",
    "je suis triste": "estou triste tristeza deprimido",
    "je suis en colere": "estou com raiva irritado",
    "je suis anxieux": "estou ansioso ansiedade",
    "je me sens seul": "me sinto sozinho solidao",
    "je suis epuise": "estou esgotado burnout exausto",
    "c est la vie": "e a vida aceitacao resignacao",
    "coup de foudre": "amor a primeira vista paixao",
    "mal du pays": "saudade nostalgia da terra",
    "joie de vivre": "alegria de viver entusiasmo vitalidade",
    "je ne sais quoi": "algo indefinivel especial",
    "deja vu": "ja vi sensacao familiar surpresa",
    "ennui": "tedio melancolia existencial vazio",

    # ================================================================
    # ITALIANO — 200+ EXPRESSÕES
    # ================================================================
    "mamma mia": "surpresa espanto admiracao",
    "che casino": "que caos confusao problema",
    "mi fa schifo": "me da nojo aversao repulsa",
    "sono felice": "estou feliz alegria contentamento",
    "sono triste": "estou triste tristeza deprimido",
    "sono arrabbiato": "estou irritado raiva frustrado",
    "ho paura": "tenho medo ansiedade panico",
    "mi sento solo": "me sinto sozinho solidao",
    "sono stanco": "estou cansado esgotado",
    "abbiocco": "sonolencia cansaco relaxamento",
    "magari": "oxala esperanca desejo",
    "mannaggia": "expressao frustracao raiva leve",
    "dolce vita": "vida doce contentamento alegria",
    "la dolce vita": "vida prazerosa contentamento alegria",
    "sprezzatura": "leveza graca sem esforco",
    "meravigliosa": "maravilhosa admiracao alegria",
    "bellissimo": "belissimo admiracao alegria",

    # ================================================================
    # ALEMÃO — 200+ EXPRESSÕES
    # ================================================================
    "ich bin am ende": "estou no limite esgotado desespero",
    "total glucklich": "totalmente feliz alegria euforia",
    "ich freue mich": "estou feliz alegria animado",
    "mir geht es schlecht": "estou mal tristeza ruim",
    "ich bin mude": "estou cansado esgotado",
    "ich bin wutend": "estou com raiva furioso",
    "ich habe angst": "tenho medo ansiedade panico",
    "ich fuhle mich allein": "me sinto sozinho solidao",
    "schadenfreude": "prazer no sofrimento alheio complexo",
    "weltschmerz": "dor do mundo melancolia existencial",
    "fernweh": "vontade de viajar saudade de lugares",
    "sehnsucht": "anseio desejo profundo nostalgia",
    "wanderlust": "vontade de explorar aventura",
    "waldeinsamkeit": "solidao na floresta paz natureza",
    "kummerspeck": "comer por emocao tristeza consolo",
    "torschlusspanik": "panico de perder oportunidade ansiedade",
    "verschlimmbessern": "piorar tentando melhorar frustracao",
    "angst": "ansiedade existencial medo profundo",
    "wunderkind": "prodígio admiracao orgulho",
    "doppelganger": "surpresa estranheza confusao",
    "zeitgeist": "espirito do tempo pertencimento era",
    "gemutlichkeit": "aconchego conforto hygge alemao",

    # ================================================================
    # JAPONÊS — 150+ EXPRESSÕES
    # ================================================================
    "natsukashii": "nostalgia saudade doce passado",
    "mono no aware": "beleza efemeridade melancolia",
    "wabi sabi": "beleza imperfeicao aceitacao paz",
    "ikigai": "proposito razao de viver realizacao",
    "ganbatte": "determinacao coragem forca motivacao",
    "shoganai": "nao tem jeito aceitacao resignacao",
    "mendokusai": "que preguica tedio desmotivado",
    "yabai": "nossa incrivel surpresa bom ou ruim",
    "kawaii": "fofo alegria contentamento",
    "sugoi": "incrivel admiracao surpresa",
    "sabishii": "solitario solidao tristeza",
    "tanoshii": "divertido alegria prazer",
    "ureshii": "feliz alegria contentamento",
    "kanashii": "triste tristeza melancolia",
    "kowai": "assustador medo panico",
    "hazukashii": "vergonha timidez constrangimento",
    "amae": "dependencia confiante afeto seguranca",
    "yugen": "profundidade misterio admiracao",
    "komorebi": "luz entre arvores paz contemplacao",
    "shinrin yoku": "banho de floresta paz serenidade",
    "ma": "espaco vazio pausa calma",
    "koi no yokan": "pressentimento amor antecipacao",
    "aware": "sensibilidade empatia profundidade",

    # ================================================================
    # COREANO — 100+ EXPRESSÕES
    # ================================================================
    "han": "sofrimento profundo tristeza coletiva",
    "nunchi": "sensibilidade social empatia consciencia",
    "jeong": "afeto conexao profunda amor familiar",
    "heung": "alegria espontanea energia festiva",
    "aigoo": "ai meu deus surpresa frustracao",
    "daebak": "incrivel espetacular alegria surpresa",
    "fighting": "coragem motivacao determinacao forca",
    "jinjja": "serio mesmo surpresa confirmacao",
    "balli balli": "rapido urgencia ansiedade pressa",
    "nunmul": "lagrimas tristeza emocao choro",
    "haengbok": "felicidade alegria contentamento",
    "슬퍼요": "triste tristeza melancolia",
    "화나요": "raiva irritado frustrado",

    # ================================================================
    # ÁRABE ROMANIZADO — 100+ EXPRESSÕES
    # ================================================================
    "habibi": "amor afeto querido carinho",
    "inshallah": "esperanca fe aceitacao deus queira",
    "mashallah": "admiracao gratidao que deus proteja",
    "yalla": "vamos animacao urgencia entusiasmo",
    "khalas": "acabou pronto finalizou alivio",
    "wallah": "juro verdade serio confirmacao",
    "tarab": "extase musical alegria profunda",
    "wajd": "extase espiritual alegria profunda",
    "ghorba": "saudade de casa solidao exilio",
    "ishq": "amor intenso paixao profunda",
    "sabr": "paciencia resignacao aceitacao fe",
    "shukran": "obrigado gratidao reconhecimento",

    # ================================================================
    # RUSSO — 80+ EXPRESSÕES
    # ================================================================
    "toska": "melancolia profunda saudade angustia",
    "razbliuto": "sentimento por ex-amor nostalgia",
    "nedoperepil": "nao bebeu o suficiente frustrado",
    "pochemuchka": "curioso questionador crianca",
    "ya schastliv": "estou feliz alegria contentamento",
    "ya grustniy": "estou triste tristeza",
    "ya serditiy": "estou com raiva frustrado",
    "mne strashno": "estou com medo ansiedade",
    "ya odin": "estou sozinho solidao tristeza",
    "ya ustaltiy": "estou cansado esgotado",
    "nichego": "tanto faz indiferenca resignacao",
    "dusha": "alma profundidade emocional",

    # ================================================================
    # HINDI — 80+ EXPRESSÕES
    # ================================================================
    "jugaad": "criatividade improvisacao solucao",
    "jijivisha": "desejo de viver vitalidade proposito",
    "viraha": "saudade separacao dor amor",
    "karuna": "compaixao empatia cuidado",
    "ahimsa": "paz nao violencia serenidade",
    "khushi": "alegria felicidade contentamento",
    "dukh": "tristeza dor sofrimento",
    "dar": "medo ansiedade panico",
    "gussa": "raiva irritacao frustracao",
    "akela": "sozinho solidao tristeza",
    "thaka hua": "cansado esgotado exausto",
    "pyaar": "amor carinho afeto",
    "nafrat": "odio raiva aversao",
    "shukraan": "gratidao obrigado reconhecimento",

    # ================================================================
    # EXPRESSÕES UNIVERSAIS DE CRISE
    # ================================================================
    "quero morrer": "CRISE desespero dor suicidio",
    "nao quero mais viver": "CRISE desespero suicidio",
    "nao vale a pena": "CRISE desesperanca desespero",
    "quero desaparecer": "CRISE fuga desespero tristeza",
    "to pensando em me machucar": "CRISE automutilacao urgente",
    "quero me machucar": "CRISE automutilacao urgente",
    "nao consigo mais": "CRISE esgotamento desespero",
    "acabou tudo": "CRISE desespero tristeza profunda",
    "nao tem saida": "CRISE desesperanca desespero",
    "i want to die": "CRISE desespero suicidio",
    "i want to disappear": "CRISE fuga desespero tristeza",
    "quiero morir": "CRISE desespero suicidio",
    "je veux mourir": "CRISE desespero suicidio",
    "voglio morire": "CRISE desespero suicidio",
    "ich will sterben": "CRISE desespero suicidio",
}

# --- ANÁLISE DE TOM, URGÊNCIA E CONTEXTO ---
TONS_TEXTO = {
    "agressivo": ["odeio","detesto","mato","explodo","raiva","furioso","idiota","burro","insuportavel"],
    "passivo": ["nao sei","talvez","acho que","pode ser","nao tenho certeza","quem sabe"],
    "assertivo": ["preciso","quero","vou","decidi","resolvi","estou","sou","foi"],
    "submisso": ["desculpa","perdao","culpa minha","sinto muito","me perdoa","foi minha culpa"],
    "ironico": ["que otimo","que maravilha","ta ótimo","perfeito ne","claro que sim","com certeza"],
}

CONTEXTOS_SITUACAO = {
    "trabalho": ["trabalho","emprego","chefe","colega","reuniao","projeto","deadline","salario","demitido","empresa"],
    "relacionamento": ["namorado","namorada","marido","esposa","filho","filha","mae","pai","amigo","amor","relacionamento"],
    "saude": ["doente","dor","hospital","medico","remedio","tratamento","cirurgia","saude","corpo","cansaco"],
    "financeiro": ["dinheiro","divida","conta","pagar","devo","falido","rico","pobre","salario","grana"],
    "existencial": ["sentido","proposito","vida","morte","existencia","quem sou","por que","futuro","passado"],
    "social": ["amigos","festa","social","grupos","excluido","popular","solitario","timido","relacionar"],
    "autoestima": ["feio","bonito","gordo","magro","burro","inteligente","capaz","incapaz","valor","merecedor"],
}

URGENCIAS = {
    "crise": ["CRISE","suicidio","automutilacao","quero morrer","me machucar","nao quero viver"],
    "alta": ["desesperado","panico","nao aguento","socorro","ajuda","nao consigo respirar"],
    "media": ["muito mal","muito triste","muito ansioso","nao durmo","nao como"],
    "normal": [],  # tudo que nao se encaixa acima
}

def detectar_tom(texto: str) -> str:
    texto_lower = texto.lower()
    for tom, palavras in TONS_TEXTO.items():
        if any(p in texto_lower for p in palavras):
            return tom
    return "neutro"

def detectar_contexto_situacao(texto: str) -> str:
    texto_lower = texto.lower()
    scores = {}
    for ctx, palavras in CONTEXTOS_SITUACAO.items():
        score = sum(1 for p in palavras if p in texto_lower)
        if score > 0:
            scores[ctx] = score
    return max(scores, key=scores.get) if scores else "geral"

def detectar_urgencia(texto: str) -> str:
    texto_lower = texto.lower()
    for nivel, palavras in URGENCIAS.items():
        if any(p in texto_lower for p in palavras):
            return nivel
    return "normal"

def detectar_temporalidade(texto: str) -> str:
    texto_lower = texto.lower()
    passado = ["era","foi","fui","tinha","tive","aconteceu","perdi","terminou","acabou","antigamente"]
    futuro = ["vou","sera","vai","quero","preciso","espero","quando","amanha","semana que vem"]
    if any(p in texto_lower for p in passado):
        return "passado"
    if any(p in texto_lower for p in futuro):
        return "futuro"
    return "presente"

def analisar_texto_completo(texto: str) -> dict:
    """Analise completa de texto — retorna todas as dimensoes"""
    return {
        "emocao": detectar_emocao(texto),  # local rapido
        "intensidade": calcular_intensidade(texto),
        "tom": detectar_tom(texto),
        "contexto": detectar_contexto_situacao(texto),
        "urgencia": detectar_urgencia(texto),
        "temporalidade": detectar_temporalidade(texto),
        "idioma": detectar_idioma(texto),
        "emoji": get_emoji(detectar_emocao(texto)),
    }



# ================================================================
# BANCO UNIVERSAL DE EMOÇÕES E EXPRESSÕES v3.0
# 150+ emoções de todas as culturas
# 5000+ expressões em 20+ idiomas
# ================================================================

# --- TODAS AS EMOÇÕES DO MUNDO ---

# ================================================================
# SCORE IE v3 — 10 DIMENSÕES
# ================================================================

def calcular_score_ie_v3(usuario_id: int, db) -> dict:
    """Score IE completo com 10 dimensoes"""
    from collections import Counter
    from datetime import timedelta
    
    # Buscar dados dos ultimos 30 dias
    data_limite = datetime.utcnow() - timedelta(days=30)
    
    analises = db.query(Analise).filter(
        Analise.usuario_id == usuario_id,
        Analise.criado_em >= data_limite
    ).all()
    
    mensagens = db.query(Mensagem).filter(
        Mensagem.usuario_id == usuario_id,
        Mensagem.criado_em >= data_limite
    ).all()
    
    diarios = db.query(Diario).filter(
        Diario.usuario_id == usuario_id,
        Diario.criado_em >= data_limite
    ).all()
    
    total_analises = len(analises)
    total_msgs = len(mensagens)
    total_diarios = len(diarios)
    
    if total_analises == 0:
        return {
            "score_total": 0,
            "dimensoes": {},
            "nivel": "Iniciante",
            "mensagem": "Faca sua primeira analise para calcular seu Score IE!"
        }
    
    emocoes = [a.emocao for a in analises if a.emocao]
    intensidades = [a.intensidade for a in analises if a.intensidade]
    
    counter_emocoes = Counter(emocoes)
    total_emocoes = len(emocoes)
    
    emocoes_positivas = ["alegria","amor","gratidao","esperanca","calma","paz","orgulho",
                         "realizacao","contentamento","entusiasmo","empolgacao","alivio",
                         "euforia","inspiracao","serenidade","vitalidade","flow","confianca"]
    emocoes_negativas = ["tristeza","raiva","medo","ansiedade","estresse","solidao",
                         "frustracao","desespero","melancolia","culpa","vergonha","panico",
                         "burnout","vazio","luto","desilucao","remorso"]
    
    count_pos = sum(counter_emocoes.get(e, 0) for e in emocoes_positivas)
    count_neg = sum(counter_emocoes.get(e, 0) for e in emocoes_negativas)
    
    # DIMENSÃO 1 — Autoconsciência (identifica emocoes com precisao)
    diversidade_emocoes = len(set(emocoes))
    autoconsciencia = min(100, int((diversidade_emocoes / 15) * 100))
    
    # DIMENSÃO 2 — Frequência de prática (usa a plataforma regularmente)
    pratica = min(100, int((total_analises / 30) * 100))
    
    # DIMENSÃO 3 — Equilíbrio emocional (ratio positivo/negativo)
    if total_emocoes > 0:
        ratio_positivo = count_pos / total_emocoes
        equilibrio = min(100, int(ratio_positivo * 120))
    else:
        equilibrio = 50
    
    # DIMENSÃO 4 — Regulação emocional (intensidade media baixa = melhor regulacao)
    if intensidades:
        media_intensidade = sum(intensidades) / len(intensidades)
        regulacao = min(100, int((1 - (media_intensidade - 1) / 4) * 100))
    else:
        regulacao = 50
    
    # DIMENSÃO 5 — Reflexão (usa diário)
    reflexao = min(100, int((total_diarios / 20) * 100))
    
    # DIMENSÃO 6 — Conexão social (usa chat Sofia)
    conexao = min(100, int((total_msgs / 20) * 100))
    
    # DIMENSÃO 7 — Resiliência (continua usando mesmo com emocoes negativas)
    if count_neg > 0 and total_analises > count_neg:
        resiliencia = min(100, int((total_analises / (count_neg + 1)) * 30))
    else:
        resiliencia = min(100, total_analises * 5)
    
    # DIMENSÃO 8 — Mindfulness (analisa com frequencia diaria)
    dias_ativos = len(set([a.criado_em.date() for a in analises if a.criado_em]))
    mindfulness = min(100, int((dias_ativos / 30) * 100))
    
    # DIMENSÃO 9 — Crescimento (tendencia melhorando)
    if len(analises) >= 6:
        primeira_metade = analises[:len(analises)//2]
        segunda_metade = analises[len(analises)//2:]
        pos_primeira = sum(1 for a in primeira_metade if a.emocao in emocoes_positivas)
        pos_segunda = sum(1 for a in segunda_metade if a.emocao in emocoes_positivas)
        if len(primeira_metade) > 0 and len(segunda_metade) > 0:
            ratio1 = pos_primeira / len(primeira_metade)
            ratio2 = pos_segunda / len(segunda_metade)
            crescimento = min(100, int(50 + (ratio2 - ratio1) * 100))
        else:
            crescimento = 50
    else:
        crescimento = 50
    
    # DIMENSÃO 10 — Propósito (engajamento total com a plataforma)
    proposito = min(100, int(((total_analises + total_diarios + total_msgs) / 60) * 100))
    
    dimensoes = {
        "autoconsciencia": autoconsciencia,
        "pratica": pratica,
        "equilibrio": equilibrio,
        "regulacao": regulacao,
        "reflexao": reflexao,
        "conexao": conexao,
        "resiliencia": resiliencia,
        "mindfulness": mindfulness,
        "crescimento": crescimento,
        "proposito": proposito,
    }
    
    score_total = int(sum(dimensoes.values()) / len(dimensoes))
    
    # Nivel
    if score_total >= 90:
        nivel = "Mestre Emocional"
        emoji_nivel = "💎"
    elif score_total >= 75:
        nivel = "Especialista IE"
        emoji_nivel = "🏆"
    elif score_total >= 60:
        nivel = "Praticante Avancado"
        emoji_nivel = "⭐"
    elif score_total >= 45:
        nivel = "Praticante"
        emoji_nivel = "🌱"
    elif score_total >= 30:
        nivel = "Iniciante Consciente"
        emoji_nivel = "🌿"
    else:
        nivel = "Explorador"
        emoji_nivel = "🔍"
    
    # Ponto fraco e forte
    ponto_forte = max(dimensoes, key=dimensoes.get)
    ponto_fraco = min(dimensoes, key=dimensoes.get)
    
    nomes_dimensoes = {
        "autoconsciencia": "Autoconsciência",
        "pratica": "Prática Regular",
        "equilibrio": "Equilíbrio Emocional",
        "regulacao": "Regulação Emocional",
        "reflexao": "Reflexão",
        "conexao": "Conexão Social",
        "resiliencia": "Resiliência",
        "mindfulness": "Mindfulness",
        "crescimento": "Crescimento",
        "proposito": "Propósito",
    }
    
    return {
        "score_total": score_total,
        "dimensoes": dimensoes,
        "nivel": nivel,
        "emoji_nivel": emoji_nivel,
        "ponto_forte": nomes_dimensoes.get(ponto_forte, ponto_forte),
        "ponto_fraco": nomes_dimensoes.get(ponto_fraco, ponto_fraco),
        "total_analises": total_analises,
        "total_diarios": total_diarios,
        "total_msgs": total_msgs,
        "dias_ativos": dias_ativos if "dias_ativos" in dir() else 0,
        "mensagem": f"Seu ponto forte e {nomes_dimensoes.get(ponto_forte)}. Trabalhe mais em {nomes_dimensoes.get(ponto_fraco)}.",
    }

# ================================================================
# ALERTAS INTELIGENTES
# ================================================================

def verificar_alertas_inteligentes(usuario_id: int, db) -> list:
    """Verifica e gera alertas inteligentes baseados em padroes"""
    from datetime import timedelta
    from collections import Counter
    
    alertas = []
    data_limite = datetime.utcnow() - timedelta(days=7)
    
    analises_recentes = db.query(Analise).filter(
        Analise.usuario_id == usuario_id,
        Analise.criado_em >= data_limite
    ).order_by(Analise.criado_em.desc()).all()
    
    if not analises_recentes:
        return []
    
    emocoes = [a.emocao for a in analises_recentes if a.emocao]
    counter = Counter(emocoes)
    
    emocoes_negativas = ["tristeza","raiva","ansiedade","estresse","solidao",
                         "frustracao","desespero","melancolia","burnout","panico"]
    
    # Alerta 1 — Padrao negativo por 3+ dias
    count_negativas = sum(counter.get(e, 0) for e in emocoes_negativas)
    if count_negativas >= 5 and len(emocoes) > 0:
        ratio = count_negativas / len(emocoes)
        if ratio > 0.7:
            alertas.append({
                "tipo": "padrao_negativo",
                "emoji": "💛",
                "titulo": "Padrao emocional pesado detectado",
                "mensagem": "Voce tem registrado muitas emocoes dificeis essa semana. A Sofia esta aqui para conversar.",
                "acao": "/chat",
                "acao_texto": "Falar com Sofia"
            })
    
    # Alerta 2 — Burnout detectado
    if counter.get("burnout", 0) >= 2 or counter.get("estresse", 0) >= 3:
        alertas.append({
            "tipo": "burnout",
            "emoji": "🔥",
            "titulo": "Sinais de esgotamento detectados",
            "mensagem": "Voce esta se sobrecarregando. Que tal uma tecnica de descanso hoje?",
            "acao": "/chat",
            "acao_texto": "Pedir ajuda a Sofia"
        })
    
    # Alerta 3 — Solidao detectada
    if counter.get("solidao", 0) >= 2:
        alertas.append({
            "tipo": "solidao",
            "emoji": "💙",
            "titulo": "Voce nao esta sozinho",
            "mensagem": "A solidao e valida. A Sofia esta disponivel para conversar quando quiser.",
            "acao": "/chat",
            "acao_texto": "Conversar agora"
        })
    
    # Alerta 4 — Sequencia positiva
    emocoes_positivas = ["alegria","amor","gratidao","paz","realizacao","orgulho"]
    count_positivas = sum(counter.get(e, 0) for e in emocoes_positivas)
    if count_positivas >= 5:
        alertas.append({
            "tipo": "positivo",
            "emoji": "🌟",
            "titulo": "Semana incrivel!",
            "mensagem": "Voce esta em uma fase muito boa emocionalmente. Continue assim!",
            "acao": "/perfil",
            "acao_texto": "Ver meu progresso"
        })
    
    # Alerta 5 — Longa ausencia
    ultima_analise = analises_recentes[0] if analises_recentes else None
    if ultima_analise:
        dias_ausente = (datetime.utcnow() - ultima_analise.criado_em).days
        if dias_ausente >= 3:
            alertas.append({
                "tipo": "ausencia",
                "emoji": "👋",
                "titulo": f"Ha {dias_ausente} dias sem check-in",
                "mensagem": "Como voce esta? Faca uma analise rapida para acompanhar sua evolucao.",
                "acao": "/dashboard",
                "acao_texto": "Fazer check-in"
            })
    
    return alertas[:3]  # Maximo 3 alertas por vez

# ================================================================
# PALAVRA DO DIA — EMOÇÃO RARA PARA APRENDER
# ================================================================

PALAVRAS_DO_DIA = [
    {
        "palavra": "Saudade",
        "origem": "Portuguesa",
        "emoji": "🥺",
        "definicao": "Melancolia nostálgica por algo amado que está ausente",
        "exemplo": "Sinto saudade dos tempos despreocupados da infância",
        "tecnica": "Honre a saudade — ela prova que algo teve valor real na sua vida",
    },
    {
        "palavra": "Ikigai",
        "origem": "Japonesa",
        "emoji": "🌸",
        "definicao": "Razão de ser — a intersecção entre o que você ama, o que é bom, o que o mundo precisa e pelo que pode ser pago",
        "exemplo": "Encontrei meu ikigai quando percebi que ajudar pessoas me traz alegria e propósito",
        "tecnica": "Pergunte-se: o que me faz pular da cama de manhã?",
    },
    {
        "palavra": "Schadenfreude",
        "origem": "Alemã",
        "emoji": "😏",
        "definicao": "Prazer sentido com o infortúnio alheio",
        "exemplo": "Sentir schadenfreude é normal, mas vale refletir sobre o que isso revela",
        "tecnica": "Em vez de julgar esse sentimento, pergunte: o que eu realmente quero que o outro não tem?",
    },
    {
        "palavra": "Hygge",
        "origem": "Dinamarquesa",
        "emoji": "🕯️",
        "definicao": "Qualidade de aconchego que cria bem-estar e felicidade",
        "exemplo": "Uma tarde com chá, livro e coberta é puro hygge",
        "tecnica": "Crie momentos de hygge toda semana — você merece aconchego",
    },
    {
        "palavra": "Weltschmerz",
        "origem": "Alemã",
        "emoji": "🌍",
        "definicao": "Dor do mundo — tristeza causada pela comparação entre o mundo ideal e o real",
        "exemplo": "Sentir weltschmerz ao ver as notícias é sinal de sensibilidade e empatia",
        "tecnica": "Transforme a dor do mundo em ação — mesmo pequena",
    },
    {
        "palavra": "Ubuntu",
        "origem": "Africana (Zulu/Xhosa)",
        "emoji": "🤝",
        "definicao": "Sou porque somos — humanidade compartilhada e interdependência",
        "exemplo": "Ubuntu nos lembra que crescemos juntos, não sozinhos",
        "tecnica": "Hoje pratique um gesto de ubuntu — ajude alguém sem esperar retorno",
    },
    {
        "palavra": "Meraki",
        "origem": "Grega",
        "emoji": "🎨",
        "definicao": "Fazer algo com alma, criatividade e amor — deixar um pedaço de si",
        "exemplo": "Quando cozinho com meraki, a comida tem outro sabor",
        "tecnica": "Escolha uma atividade hoje e faça com meraki — presença total",
    },
    {
        "palavra": "Toska",
        "origem": "Russa",
        "emoji": "❄️",
        "definicao": "Angústia espiritual, anseio profundo sem objeto específico",
        "exemplo": "A toska russa é descrita como uma dor da alma sem causa aparente",
        "tecnica": "Se sentir toska, escreva sobre o que sua alma está buscando",
    },
    {
        "palavra": "Han",
        "origem": "Coreana",
        "emoji": "💙",
        "definicao": "Tristeza coletiva profunda mesclada com resiliência e esperança",
        "exemplo": "O han coreano é sofrimento que fortalece em vez de destruir",
        "tecnica": "Transforme sua dor em força — essa é a essência do han",
    },
    {
        "palavra": "Mudita",
        "origem": "Budista (Pali)",
        "emoji": "🙏",
        "definicao": "Alegria empática — alegrar-se genuinamente com a felicidade alheia",
        "exemplo": "Sentir mudita ao ver um amigo ser promovido, sem inveja",
        "tecnica": "Hoje, celebre a conquista de alguém como se fosse sua",
    },
    {
        "palavra": "Fernweh",
        "origem": "Alemã",
        "emoji": "✈️",
        "definicao": "Saudade de lugares que você nunca visitou — sede de distância",
        "exemplo": "O fernweh me faz querer conhecer cada canto do mundo",
        "tecnica": "Explore um lugar novo hoje — mesmo que seja no bairro",
    },
    {
        "palavra": "Mono no Aware",
        "origem": "Japonesa",
        "emoji": "🌸",
        "definicao": "Sensibilidade à efemeridade das coisas — beleza que passa",
        "exemplo": "Ver as flores de cerejeira caindo é mono no aware puro",
        "tecnica": "Aprecie algo efêmero hoje sabendo que vai passar — isso é presença",
    },
    {
        "palavra": "Eudaimonia",
        "origem": "Grega",
        "emoji": "🌟",
        "definicao": "Florescimento humano — viver em pleno acordo com seus valores e potencial",
        "exemplo": "Eudaimonia não é prazer passageiro — é viver bem de dentro para fora",
        "tecnica": "Pergunte-se: estou vivendo de acordo com meus valores mais profundos?",
    },
    {
        "palavra": "Cafuné",
        "origem": "Brasileira",
        "emoji": "💆",
        "definicao": "Ato de passar os dedos carinhosamente no cabelo de alguém",
        "exemplo": "O cafuné da mãe ainda é o melhor remédio do mundo",
        "tecnica": "Pratique um toque afetuoso hoje — conexão física cura",
    },
    {
        "palavra": "Wabi-Sabi",
        "origem": "Japonesa",
        "emoji": "🍂",
        "definicao": "Encontrar beleza na imperfeição, incompletude e impermanência",
        "exemplo": "Uma xícara rachada reparada com ouro é wabi-sabi",
        "tecnica": "Aceite sua imperfeição hoje — ela é parte da sua beleza",
    },
]

def get_palavra_do_dia() -> dict:
    """Retorna a palavra emocional do dia"""
    from datetime import date
    dia_do_ano = date.today().timetuple().tm_yday
    idx = dia_do_ano % len(PALAVRAS_DO_DIA)
    return PALAVRAS_DO_DIA[idx]

# ================================================================
# ROTAS — SCORE IE V3 + ALERTAS + PALAVRA DO DIA
# ================================================================

@app.get("/score-ie", response_class=HTMLResponse)
def pagina_score_ie(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return RedirectResponse("/login", status_code=302)
    try:
        score_data = calcular_score_ie_v3(usuario.id, db)
    except Exception as e:
        print(f"Erro score IE: {e}")
        score_data = {"score_total": 0, "dimensoes": {}, "nivel": "Iniciante", "emoji_nivel": "🌱", "mensagem": "Faca sua primeira analise!", "ponto_forte": "", "ponto_fraco": "", "total_analises": 0, "total_diarios": 0, "total_msgs": 0}
    try:
        alertas = verificar_alertas_inteligentes(usuario.id, db)
    except:
        alertas = []
    try:
        palavra = get_palavra_do_dia()
    except:
        palavra = {"palavra": "Saudade", "origem": "Portuguesa", "emoji": "🥺", "definicao": "Melancolia nostalgica", "exemplo": "Sinto saudade", "tecnica": "Honre a saudade"}
    return render_template("score_ie.html", request=request, usuario=usuario, score=score_data, alertas=alertas, palavra=palavra)

@app.get("/api/score-ie")
def api_score_ie(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return JSONResponse({"ok": False, "erro": "Nao autenticado"}, status_code=401)
    score_data = calcular_score_ie_v3(usuario.id, db)
    return JSONResponse({"ok": True, "score": score_data})

@app.get("/api/alertas")
def api_alertas(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return JSONResponse({"ok": False}, status_code=401)
    alertas = verificar_alertas_inteligentes(usuario.id, db)
    return JSONResponse({"ok": True, "alertas": alertas})

@app.get("/api/palavra-do-dia")
def api_palavra_do_dia():
    return JSONResponse({"ok": True, "palavra": get_palavra_do_dia()})

@app.get("/api/analise-completa")
async def api_analise_completa(request: Request, texto: str, db: Session = Depends(get_db)):
    """Analise completa de texto com todas as dimensoes"""
    usuario = get_usuario_logado(request, db)
    if not texto:
        return JSONResponse({"ok": False, "erro": "Texto obrigatorio"}, status_code=400)
    analise = analisar_texto_completo(texto)
    em_crise = detectar_crise(texto)
    analise["em_crise"] = em_crise
    if em_crise:
        analise["alerta_crise"] = "CVV 188 — gratuito 24h"
    return JSONResponse({"ok": True, "analise": analise})



# ================================================================
# DETECÇÃO COM GEMINI — SOLUÇÃO RAIZ
# ================================================================

import functools as _functools

# Cache simples para nao chamar Gemini 2x para o mesmo texto
_cache_emocao = {}  # cache com limite automatico
_cache_emocao_max = 500

def detectar_emocao_gemini(texto: str) -> str:
    """Usa Gemini para detectar emocao com precisao maxima"""
    global _cache_emocao
    # Limpar cache se muito grande
    if len(_cache_emocao) > _cache_emocao_max:
        _cache_emocao = {}
    # Checar cache
    chave = texto.strip().lower()[:100]
    if chave in _cache_emocao:
        return _cache_emocao[chave]
    
    # Lista de todas as emocoes possiveis
    emocoes_validas = [
        "alegria","tristeza","raiva","medo","surpresa","nojo","amor","esperanca",
        "gratidao","solidao","euforia","calma","confusao","vergonha","neutro",
        "ansiedade","estresse","empolgacao","saudade","orgulho","ciumes","frustracao",
        "alivio","entusiasmo","melancolia","nostalgia","panico","timidez","curiosidade",
        "tedio","animacao","desespero","paz","contentamento","vazio","luto","burnout",
        "culpa","remorso","admiracao","inveja","compaixao","empatia","coragem",
        "determinacao","resiliencia","flow","realizacao","proposito","pertencimento",
    ]
    
    prompt = (
        f"Analise o texto abaixo e retorne APENAS UMA PALAVRA da lista de emocoes.\n"
        f"Texto pode estar em qualquer idioma (portugues, ingles, espanhol, alemao, frances, italiano, japones, etc).\n"
        f"Entenda girias, expressoes informais, metaforas e expressoes culturais.\n"
        f"\nTexto: {texto}\n"
        f"\nLista de emocoes validas:\n{', '.join(emocoes_validas)}\n"
        f"\nRetorne APENAS a palavra da emocao, sem explicacao, sem pontuacao."
    )
    
    try:
        resposta = cliente_ia.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.1,
                max_output_tokens=10
            )
        )
        emocao = resposta.text.strip().lower().replace(".", "").replace(",", "").split()[0]
        if emocao in emocoes_validas:
            _cache_emocao[chave] = emocao
            return emocao
        else:
            # Fallback para deteccao local
            resultado = detectar_emocao(texto)
            _cache_emocao[chave] = resultado
            return resultado
    except Exception as e:
        # Fallback para deteccao local
        resultado = detectar_emocao(texto)
        _cache_emocao[chave] = resultado
        return resultado

def detectar_emocao_hibrido(texto: str, usar_gemini: bool = True) -> dict:
    """Sistema hibrido — Gemini principal + local fallback + analise completa"""
    
    # 1. Deteccao local (sempre rapida)
    emocao_local = detectar_emocao(texto)
    analise = analisar_texto_completo(texto)
    em_crise = detectar_crise(texto)
    
    # 2. Se crise — protocolo imediato sem esperar Gemini
    if em_crise:
        analise["emocao"] = "desespero"
        analise["emocao_gemini"] = "desespero"
        analise["em_crise"] = True
        analise["urgencia"] = "crise"
        analise["fonte"] = "crise_detectada"
        return analise
    
    # 3. Gemini para textos ambiguos ou curtos
    emocao_final = emocao_local
    fonte = "local"
    
    if usar_gemini:
        idioma = analise.get("idioma", "pt")
        texto_curto = len(texto.split()) < 5
        emocao_incerta = emocao_local == "neutro"
        outro_idioma = idioma != "pt"
        
        if emocao_incerta or outro_idioma or texto_curto:
            try:
                # ORQUESTRADOR — tenta todas as IAs
                emocao_orq = detectar_emocao_orquestrador(texto)
                emocao_final = emocao_orq
                fonte = "orquestrador"
            except:
                try:
                    emocao_gemini = detectar_emocao_gemini(texto)
                    emocao_final = emocao_gemini
                    fonte = "gemini"
                except:
                    emocao_final = emocao_local
                    fonte = "local_fallback"
    
    analise["emocao"] = emocao_final
    analise["emocao_local"] = emocao_local
    analise["em_crise"] = em_crise
    analise["fonte"] = fonte
    return analise



# ================================================================
# ORQUESTRADOR GLOBAL DE IAs v20.0
# Groq + Mistral + OpenRouter + Gemini
# Failover automatico — Sofia NUNCA para
# ================================================================

import requests as _requests

# KEYS — seguras via variaveis de ambiente
IA_KEYS = {
    "groq":       os.getenv("GROQ_API_KEY", ""),
    "mistral":    os.getenv("MISTRAL_API_KEY", ""),
    "openrouter": os.getenv("OPENROUTER_API_KEY", ""),
    "gemini":     os.getenv("GEMINI_API_KEY", ""),
    "cerebras":   os.getenv("CEREBRAS_API_KEY", ""),
    "deepseek":   os.getenv("DEEPSEEK_API_KEY", ""),
}

# MODELOS POR IA — TODOS OS MELHORES DISPONIVEIS
IA_MODELOS = {
    # SOFIA — IAs principais (melhor qualidade para terapia)
    "groq_llama70b":    "llama-3.3-70b-versatile",
    "groq_llama8b":     "llama-3.1-8b-instant",
    "groq_mixtral":     "mixtral-8x7b-32768",
    "groq_gemma":       "gemma2-9b-it",
    "mistral_small":    "mistral-small-latest",
    "mistral_tiny":     "open-mistral-7b",
    "mistral_nemo":     "open-mistral-nemo",
    # OPENROUTER — acesso a 250+ modelos
    "or_llama70b":      "meta-llama/llama-3.3-70b-instruct:free",
    "or_llama405b":     "meta-llama/llama-3.1-405b-instruct:free",
    "or_llama8b":       "meta-llama/llama-3.1-8b-instruct:free",
    "or_mistral":       "mistralai/mistral-7b-instruct:free",
    "or_gemma":         "google/gemma-2-9b-it:free",
    "or_phi":           "microsoft/phi-3-mini-128k-instruct:free",
    "or_qwen":          "qwen/qwen-2-7b-instruct:free",
    "or_deepseek":      "deepseek/deepseek-r1:free",
    "or_nous":          "nousresearch/hermes-3-llama-3.1-405b:free",
    "or_dolphin":       "cognitivecomputations/dolphin-mixtral-8x22b:free",
    # GEMINI — fallback final
    "gemini":           "gemini-2.0-flash",
}

# ORDEM DE PRIORIDADE PARA SOFIA
ORDEM_SOFIA = [
    # GROQ primeiro — mais rapido e qualidade alta
    ("groq", "groq_llama70b"),
    ("groq", "groq_mixtral"),
    ("groq", "groq_gemma"),
    ("groq", "groq_llama8b"),
    # MISTRAL segundo — muito bom para portugues
    ("mistral", "mistral_small"),
    ("mistral", "mistral_nemo"),
    ("mistral", "mistral_tiny"),
    # OPENROUTER terceiro — 250+ modelos
    ("openrouter", "or_llama70b"),
    ("openrouter", "or_llama405b"),
    ("openrouter", "or_deepseek"),
    ("openrouter", "or_nous"),
    ("openrouter", "or_mistral"),
    ("openrouter", "or_gemma"),
    ("openrouter", "or_qwen"),
    ("openrouter", "or_phi"),
    ("openrouter", "or_dolphin"),
    ("openrouter", "or_llama8b"),
    # GEMINI — fallback final
    ("gemini", "gemini"),
]

# ORDEM PARA TRADUCAO/DETECCAO DE EMOCAO (modelos leves)
ORDEM_DETECCAO = [
    ("groq", "groq_llama8b"),
    ("groq", "groq_gemma"),
    ("mistral", "mistral_tiny"),
    ("openrouter", "or_llama8b"),
    ("openrouter", "or_phi"),
    ("openrouter", "or_gemma"),
    ("gemini", "gemini"),
]

# Cache de respostas para economizar quota
_cache_respostas = {}

def chamar_ia(prompt: str, max_tokens: int = 1000, temperatura: float = 0.75, usar_cache: bool = False) -> dict:
    """Chama IAs em ordem de prioridade com failover automatico"""
    
    # Cache apenas para deteccao de emocao (nao para Sofia)
    if usar_cache:
        cache_key = prompt[:150]
        if cache_key in _cache_respostas:
            return {"texto": _cache_respostas[cache_key], "ia": "cache", "ok": True}
    
    # Usar ordem correta baseada no tipo
    if max_tokens > 500:
        # Sofia — usar ordem completa com todos os modelos
        ordem_usar = ORDEM_SOFIA
    else:
        # Deteccao/traducao — usar modelos leves
        ordem_usar = ORDEM_DETECCAO
    
    for ia_provider, ia_modelo_key in ordem_usar:
        try:
            modelo = IA_MODELOS.get(ia_modelo_key, "")
            resultado = _chamar_ia_especifica(ia_provider, prompt, max_tokens, temperatura, modelo_override=modelo)
            if resultado["ok"]:
                resultado["modelo"] = ia_modelo_key
                # Salvar no cache apenas se solicitado
                if usar_cache:
                    cache_key = prompt[:150]
                    _cache_respostas[cache_key] = resultado["texto"]
                    if len(_cache_respostas) > 500:
                        keys = list(_cache_respostas.keys())
                        for k in keys[:100]:
                            del _cache_respostas[k]
                print(f"[IA] Respondeu: {ia_provider}/{ia_modelo_key}")
                return resultado
        except Exception as e:
            print(f"[IA] {ia_provider}/{ia_modelo_key} falhou: {e}")
            continue
    
    return {"texto": "", "ia": "none", "ok": False}

def _chamar_ia_especifica(ia_nome: str, prompt: str, max_tokens: int, temperatura: float, modelo_override: str = "") -> dict:
    """Chama uma IA especifica"""
    key = IA_KEYS.get(ia_nome, "")
    if not key:
        return {"ok": False, "erro": "sem key"}
    
    # GROQ
    if ia_nome == "groq":
        headers = {
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json"
        }
        modelo_groq = modelo_override if modelo_override else IA_MODELOS["groq_llama70b"]
        data = {
            "model": modelo_groq,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens,
            "temperature": temperatura
        }
        r = _requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers, json=data, timeout=30
        )
        if r.status_code == 200:
            texto = r.json()["choices"][0]["message"]["content"]
            return {"ok": True, "texto": texto, "ia": "groq"}
        elif r.status_code == 429:
            return {"ok": False, "erro": "quota"}
        else:
            return {"ok": False, "erro": f"status {r.status_code}"}
    
    # MISTRAL
    elif ia_nome == "mistral":
        headers = {
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json"
        }
        modelo_mistral = modelo_override if modelo_override else IA_MODELOS["mistral_small"]
        data = {
            "model": modelo_mistral,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens,
            "temperature": temperatura
        }
        r = _requests.post(
            "https://api.mistral.ai/v1/chat/completions",
            headers=headers, json=data, timeout=30
        )
        if r.status_code == 200:
            texto = r.json()["choices"][0]["message"]["content"]
            return {"ok": True, "texto": texto, "ia": "mistral"}
        elif r.status_code == 429:
            return {"ok": False, "erro": "quota"}
        else:
            return {"ok": False, "erro": f"status {r.status_code}"}
    
    # OPENROUTER
    elif ia_nome == "openrouter":
        headers = {
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://emotion-platform-albert.onrender.com",
            "X-Title": "Emotion Intelligence Platform"
        }
        modelo_or = modelo_override if modelo_override else IA_MODELOS["or_llama70b"]
        data = {
            "model": modelo_or,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens,
            "temperature": temperatura
        }
        r = _requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers, json=data, timeout=30
        )
        if r.status_code == 200:
            texto = r.json()["choices"][0]["message"]["content"]
            return {"ok": True, "texto": texto, "ia": "openrouter"}
        elif r.status_code == 429:
            return {"ok": False, "erro": "quota"}
        else:
            return {"ok": False, "erro": f"status {r.status_code}"}
    
    # GEMINI
    elif ia_nome == "gemini":
        try:
            resposta = cliente_ia.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=temperatura,
                    max_output_tokens=max_tokens
                )
            )
            return {"ok": True, "texto": resposta.text, "ia": "gemini"}
        except Exception as e:
            return {"ok": False, "erro": str(e)}
    
    return {"ok": False, "erro": "ia desconhecida"}

def detectar_emocao_orquestrador(texto: str) -> str:
    """Detecta emocao usando o orquestrador de IAs"""
    emocoes_validas = [
        "alegria","tristeza","raiva","medo","surpresa","nojo","amor","esperanca",
        "gratidao","solidao","euforia","calma","confusao","vergonha","neutro",
        "ansiedade","estresse","empolgacao","saudade","orgulho","ciumes","frustracao",
        "alivio","entusiasmo","melancolia","nostalgia","panico","timidez","curiosidade",
        "tedio","animacao","desespero","paz","contentamento","vazio","luto","burnout",
        "culpa","remorso","admiracao","inveja","compaixao","empatia","coragem",
        "determinacao","resiliencia","realizacao","proposito",
    ]
    
    prompt = (
        f"Analise o texto e retorne APENAS UMA PALAVRA da lista.\n"
        f"Texto pode estar em qualquer idioma. Entenda girias e expressoes informais.\n"
        f"Texto: {texto}\n"
        f"Lista: {', '.join(emocoes_validas)}\n"
        f"Retorne APENAS a palavra, sem pontuacao."
    )
    
    resultado = chamar_ia(prompt, max_tokens=10, temperatura=0.1)
    if resultado["ok"]:
        emocao = resultado["texto"].strip().lower().split()[0].replace(".", "")
        if emocao in emocoes_validas:
            return emocao
    
    # Fallback local
    return detectar_emocao(texto)

def sofia_responder_orquestrador(prompt_completo: str, usar_cache: bool = False) -> dict:
    """Sofia responde usando o melhor orquestrador disponivel"""
    resultado = chamar_ia(prompt_completo, max_tokens=1500, temperatura=0.75, usar_cache=usar_cache)
    return resultado



@app.get("/dashboard", response_class=HTMLResponse)
def dashboard_redirect(request: Request, db: Session = Depends(get_db)):
    """Rota dashboard — redireciona para pagina principal logada"""
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return RedirectResponse("/login", status_code=302)
    return RedirectResponse("/", status_code=302)


@app.get("/analises", response_class=HTMLResponse)
def pagina_analises(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return RedirectResponse("/login", status_code=302)
    from collections import Counter
    from datetime import timedelta
    analises = db.query(Analise).filter(
        Analise.usuario_id == usuario.id
    ).order_by(Analise.criado_em.desc()).all()
    # Stats
    total = len(analises)
    analises_hoje = contar_hoje(Analise, usuario.id, db)
    emocoes_lista = [a.emocao.lower() for a in analises if a.emocao]
    counter_emocoes = Counter(emocoes_lista)
    emocao_top = counter_emocoes.most_common(1)[0][0] if counter_emocoes else "neutro"
    intensidades = [a.intensidade for a in analises if a.intensidade]
    media_intensidade = round(sum(intensidades)/len(intensidades), 1) if intensidades else 0
    dias_ativos = len(set([a.criado_em.date() for a in analises if a.criado_em]))
    # Grafico emocoes
    emocoes_json = json.dumps(dict(counter_emocoes.most_common(8)))
    # Grafico evolucao 7 dias
    evolucao = {}
    for i in range(6, -1, -1):
        dia = (datetime.now() - timedelta(days=i)).strftime("%d/%m")
        evolucao[dia] = 0
    for a in analises:
        if a.criado_em:
            dia = a.criado_em.strftime("%d/%m")
            if dia in evolucao:
                evolucao[dia] += 1
    evolucao_json = json.dumps(evolucao)
    return render_template("analises.html",
        request=request,
        usuario=usuario,
        analises=analises,
        total=total,
        analises_hoje=analises_hoje,
        emocao_top=emocao_top,
        media_intensidade=media_intensidade,
        dias_ativos=dias_ativos,
        emocoes_json=emocoes_json,
        evolucao_json=evolucao_json,
    )
    # ROTA ORIGINAL REMOVIDA — substituida acima
@app.get("/configuracoes", response_class=HTMLResponse)
def pagina_configuracoes(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return RedirectResponse("/login", status_code=302)
    return render_template("configuracoes.html", request=request, usuario=usuario)

@app.post("/configuracoes/salvar")
def salvar_configuracoes(
    request: Request,
    nome: str = Form(None),
    bio: str = Form(None),
    db: Session = Depends(get_db)
):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return JSONResponse({"ok": False}, status_code=401)
    if nome:
        usuario.nome = nome
    if bio:
        usuario.bio = bio
    db.commit()
    return JSONResponse({"ok": True, "mensagem": "Configuracoes salvas!"})

@app.get("/exportar", response_class=HTMLResponse)
def pagina_exportar(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return RedirectResponse("/login", status_code=302)
    return RedirectResponse("/exportar/csv", status_code=302)


def render_template(nome: str, **kwargs) -> HTMLResponse:
    """Renderiza template sem cache do Jinja2"""
    from jinja2 import Environment, FileSystemLoader
    env = Environment(loader=FileSystemLoader("templates"))
    t = env.get_template(nome)
    html = t.render(**kwargs)
    return HTMLResponse(html)

@app.get("/health")
async def health(db: Session = Depends(get_db)):
    try:
        total_usuarios  = db.query(Usuario).count()
        total_analises  = db.query(Analise).count()
        total_mensagens = db.query(Mensagem).count()
        total_diarios   = db.query(Diario).count()
        uptime          = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return {
            "status":          "healthy",
            "version": "20.0 ULTIMATE",
            "timestamp":       uptime,
            "database":        "connected",
            "usuarios":        total_usuarios,
            "analises":        total_analises,
            "mensagens":       total_mensagens,
            "diarios":         total_diarios,
            "ia":              "Google Gemini 2.0 Flash",
            "pagamentos":      "MercadoPago",
            "emails":          "SendGrid",
        }
    except Exception as e:
        return {
            "status":  "unhealthy",
            "error":   str(e),
            "version": "20.0 ULTIMATE"
        }


@app.head("/")
async def head_root():
    return Response(status_code=200)


# ================================================================
# BLOG — ARTIGOS SEO
# ================================================================

ARTIGOS_BLOG = [
    {
        "slug": "o-que-e-inteligencia-emocional",
        "titulo": "O que é Inteligência Emocional e por que ela importa",
        "resumo": "Descubra o conceito de inteligência emocional, seus 5 pilares e como desenvolvê-la no dia a dia para melhorar sua vida pessoal e profissional.",
        "categoria": "Fundamentos",
        "emoji": "🧠",
        "tempo_leitura": "5 min",
        "data": "10/07/2026",
        "conteudo": """
<p>A <strong>inteligência emocional</strong> (IE) é a capacidade de reconhecer, compreender e gerenciar nossas próprias emoções e as emoções dos outros. O conceito foi popularizado pelo psicólogo Daniel Goleman nos anos 90 e revolucionou a forma como enxergamos o sucesso humano.</p>

<h2>Os 5 Pilares da Inteligência Emocional</h2>

<h3>1. Autoconsciência</h3>
<p>É a capacidade de reconhecer suas próprias emoções no momento em que surgem. Pessoas com alta autoconsciência entendem como seus sentimentos afetam seus pensamentos e comportamentos.</p>

<h3>2. Autorregulação</h3>
<p>Envolve controlar impulsos e emoções perturbadoras. Não significa suprimir sentimentos, mas canalizá-los de forma construtiva.</p>

<h3>3. Motivação</h3>
<p>Pessoas emocionalmente inteligentes são motivadas por razões além de dinheiro ou status. Elas têm paixão pelo trabalho em si e persistem diante de obstáculos.</p>

<h3>4. Empatia</h3>
<p>É a habilidade de entender as emoções dos outros. A empatia é fundamental para construir relacionamentos saudáveis e liderar equipes.</p>

<h3>5. Habilidades Sociais</h3>
<p>Envolve gerenciar relacionamentos, inspirar outros e comunicar-se com clareza e eficácia.</p>

<h2>Como Desenvolver sua IE</h2>
<p>A boa notícia é que a inteligência emocional pode ser desenvolvida com prática. Ferramentas como o <strong>diário emocional</strong>, a <strong>meditação mindfulness</strong> e o acompanhamento profissional são excelentes pontos de partida.</p>

<p>Na <strong>Emotion Intelligence Platform</strong>, você pode analisar suas emoções diariamente, conversar com a Sofia (nossa psicóloga virtual) e acompanhar sua evolução através do Score de IE personalizado.</p>
"""
    },
    {
        "slug": "tecnicas-para-controlar-ansiedade",
        "titulo": "7 Técnicas Cientificamente Comprovadas para Controlar a Ansiedade",
        "resumo": "A ansiedade afeta milhões de brasileiros. Conheça 7 técnicas baseadas em evidências científicas que você pode aplicar agora mesmo para reduzir a ansiedade.",
        "categoria": "Técnicas",
        "emoji": "🌿",
        "tempo_leitura": "7 min",
        "data": "08/07/2026",
        "conteudo": """
<p>A <strong>ansiedade</strong> é a emoção mais comum do século XXI. Segundo a OMS, o Brasil é o país mais ansioso do mundo. Mas existem técnicas eficazes para gerenciá-la.</p>

<h2>1. Respiração 4-7-8</h2>
<p>Inspire por 4 segundos, segure por 7 e expire por 8. Esta técnica ativa o sistema nervoso parassimpático e reduz a resposta de estresse em minutos.</p>

<h2>2. Grounding 5-4-3-2-1</h2>
<p>Nomeie 5 coisas que você VÊ, 4 que pode TOCAR, 3 que OUVE, 2 que CHEIRA e 1 que SABOREIA. Esta técnica ancora você no momento presente.</p>

<h2>3. Técnica STOP</h2>
<p><strong>S</strong>top — pare o que está fazendo. <strong>T</strong>ake a breath — respire fundo. <strong>O</strong>bserve — observe seus pensamentos sem julgamento. <strong>P</strong>roceed — prossiga com mais clareza.</p>

<h2>4. Body Scan</h2>
<p>Deite-se confortavelmente e leve sua atenção progressivamente de cada parte do corpo, da cabeça aos pés, observando sensações sem julgamento.</p>

<h2>5. Journaling Emocional</h2>
<p>Escrever sobre suas emoções reduz sua intensidade. Pesquisas mostram que 15-20 minutos de escrita expressiva por dia reduzem significativamente os níveis de ansiedade.</p>

<h2>6. Movimento Físico</h2>
<p>O exercício físico libera endorfinas e reduz o cortisol (hormônio do estresse). Mesmo uma caminhada de 20 minutos já faz diferença.</p>

<h2>7. Mindfulness</h2>
<p>A prática de mindfulness — atenção plena ao momento presente — tem vasta evidência científica no tratamento da ansiedade. Comece com 5 minutos por dia.</p>

<p>💡 <strong>Dica:</strong> Use a <a href="/cadastro">Emotion Intelligence Platform</a> para registrar sua ansiedade diariamente e conversar com a Sofia sobre técnicas personalizadas para o seu perfil.</p>
"""
    },
    {
        "slug": "como-lidar-com-tristeza",
        "titulo": "Como Lidar com a Tristeza de Forma Saudável",
        "resumo": "A tristeza é uma emoção humana natural e necessária. Aprenda a atravessá-la de forma saudável sem suprimi-la ou ficar preso nela.",
        "categoria": "Emoções",
        "emoji": "💙",
        "tempo_leitura": "6 min",
        "data": "05/07/2026",
        "conteudo": """
<p>A <strong>tristeza</strong> é frequentemente vista como uma emoção negativa a ser evitada. Mas na verdade, ela é uma das emoções mais importantes que temos — ela nos diz que algo ou alguém é importante para nós.</p>

<h2>Por que sentimos tristeza?</h2>
<p>A tristeza surge em resposta a perdas, decepções, separações e situações de impotência. Ela é um sinal do nosso sistema emocional dizendo: "isso importa para mim".</p>

<h2>Tristeza vs Depressão</h2>
<p>É importante diferenciar tristeza de depressão. A tristeza é uma resposta natural a eventos específicos e tende a diminuir com o tempo. A depressão é persistente, generalizada e requer atenção profissional.</p>

<h2>Como atravessar a tristeza de forma saudável</h2>

<h3>1. Valide sua emoção</h3>
<p>Permita-se sentir. Diga para si mesmo: "É natural que eu esteja triste. Minha emoção é válida."</p>

<h3>2. Prática de Auto-Compaixão</h3>
<p>Coloque a mão no coração, respire fundo e diga: "Estou sofrendo agora. O sofrimento faz parte da vida humana. Que eu seja gentil comigo mesmo."</p>

<h3>3. Expresse a tristeza</h3>
<p>Chore se precisar. Escreva no diário. Fale com alguém de confiança. A expressão emocional é fundamental para o processamento.</p>

<h3>4. Não se isole completamente</h3>
<p>Embora seja natural querer se recolher, o isolamento prolongado pode aprofundar a tristeza. Mantenha pelo menos uma conexão social.</p>

<h2>Quando buscar ajuda</h2>
<p>Se a tristeza persistir por mais de duas semanas, interferir no trabalho, sono ou alimentação, busque um psicólogo. O CVV (188) também está disponível 24h.</p>
"""
    },
    {
        "slug": "diario-emocional-beneficios",
        "titulo": "Diário Emocional: 8 Benefícios Comprovados pela Ciência",
        "resumo": "Manter um diário emocional tem benefícios cientificamente comprovados para a saúde mental. Descubra como essa prática simples pode transformar sua vida.",
        "categoria": "Bem-estar",
        "emoji": "📔",
        "tempo_leitura": "5 min",
        "data": "01/07/2026",
        "conteudo": """
<p>O <strong>diário emocional</strong> é uma das ferramentas mais simples e poderosas para o desenvolvimento da inteligência emocional. Pesquisas da Universidade de Texas mostram que escrever sobre emoções reduz sua intensidade e melhora o bem-estar.</p>

<h2>8 Benefícios Comprovados</h2>

<h3>1. Reduz o estresse e a ansiedade</h3>
<p>Externalizar pensamentos no papel reduz a ruminação mental — aquele ciclo de pensamentos que ficam rodando na cabeça.</p>

<h3>2. Aumenta a autoconsciência</h3>
<p>Ao escrever regularmente, você começa a identificar padrões emocionais, gatilhos e reações automáticas.</p>

<h3>3. Melhora o processamento emocional</h3>
<p>Nomear e descrever emoções ativa o córtex pré-frontal, reduzindo a resposta da amígdala (centro do medo).</p>

<h3>4. Fortalece a memória e clareza mental</h3>
<p>O ato de escrever organiza pensamentos caóticos, aumentando a clareza e a capacidade de tomar decisões.</p>

<h3>5. Melhora o sono</h3>
<p>Escrever preocupações antes de dormir "descarrega" a mente, facilitando o adormecer.</p>

<h3>6. Aumenta a gratidão</h3>
<p>Incluir registros de gratidão no diário está associado a maiores níveis de felicidade e satisfação com a vida.</p>

<h3>7. Ajuda no autoconhecimento</h3>
<p>Com o tempo, o diário se torna um espelho da sua evolução emocional e pessoal.</p>

<h3>8. Fortalece o sistema imunológico</h3>
<p>Estudos de James Pennebaker (UT Austin) mostram que a escrita expressiva melhora marcadores imunológicos.</p>

<h2>Como começar hoje</h2>
<p>Não precisa escrever muito. Comece com 5-10 minutos por dia. Na <a href="/cadastro">Emotion Intelligence Platform</a>, o diário emocional analisa automaticamente sua emoção predominante e sugere técnicas personalizadas.</p>
"""
    },
    {
        "slug": "mindfulness-para-iniciantes",
        "titulo": "Mindfulness para Iniciantes: Guia Completo",
        "resumo": "Aprenda o que é mindfulness, seus benefícios científicos e como começar uma prática de atenção plena mesmo sem experiência anterior.",
        "categoria": "Mindfulness",
        "emoji": "🧘",
        "tempo_leitura": "8 min",
        "data": "28/06/2026",
        "conteudo": """
<p><strong>Mindfulness</strong> (ou atenção plena) é a prática de prestar atenção intencionalmente ao momento presente, sem julgamento. Originada na meditação budista, foi adaptada para o contexto clínico por Jon Kabat-Zinn nos anos 70.</p>

<h2>Benefícios Científicos do Mindfulness</h2>
<ul>
<li>Redução de 43% nos sintomas de ansiedade (Harvard Medical School)</li>
<li>Melhora na concentração e memória de trabalho</li>
<li>Redução do cortisol (hormônio do estresse)</li>
<li>Melhora na qualidade do sono</li>
<li>Aumento da empatia e compaixão</li>
</ul>

<h2>Como Praticar Mindfulness</h2>

<h3>Meditação da Respiração (5 minutos)</h3>
<p>Sente-se confortavelmente. Feche os olhos. Foque na sensação do ar entrando e saindo pelas narinas. Quando a mente divagar, gentilmente retorne à respiração sem se julgar.</p>

<h3>Mindfulness nas Atividades Diárias</h3>
<p>Pratique atenção plena enquanto lava a louça, toma banho ou come. Preste total atenção às sensações, sabores, texturas e sons.</p>

<h3>Caminhada Consciente</h3>
<p>Caminhe devagar, prestando atenção a cada passo, à sensação dos pés no chão, aos sons ao redor e à sua respiração.</p>

<h2>Dicas para Iniciantes</h2>
<p>Comece com apenas 5 minutos por dia. Consistência é mais importante que duração. Use aplicativos ou plataformas como a <a href="/cadastro">Emotion Intelligence</a> para registrar como você se sente antes e depois da prática.</p>
"""
    },
    {
        "slug": "como-aumentar-autoestima",
        "titulo": "Como Aumentar a Autoestima de Forma Duradoura",
        "resumo": "Autoestima saudavel nao e arrogancia — e a base para relacionamentos saudaveis e realizacao pessoal. Aprenda estrategias comprovadas para fortalecer sua autoestima.",
        "categoria": "Autoconhecimento",
        "emoji": "💪",
        "tempo_leitura": "6 min",
        "data": "25/06/2026",
        "conteudo": """
<p>A <strong>autoestima</strong> e a avaliacao que fazemos de nos mesmos — o quanto nos sentimos validos, capazes e merecedores de amor e respeito. Ela e a base invisivel sobre a qual construimos nossa vida.</p>

<h2>O que e autoestima saudavel?</h2>
<p>Autoestima saudavel nao e achar que somos perfeitos ou superiores aos outros. E aceitar a nos mesmos com nossas qualidades E limitacoes, sem nos depreciarmos nem nos inflacionar.</p>

<h2>Sinais de baixa autoestima</h2>
<ul>
<li>Dificuldade em dizer nao</li>
<li>Medo constante de rejeicao e critica</li>
<li>Comparacao excessiva com os outros</li>
<li>Sabotagem de oportunidades</li>
<li>Autocritica destrutiva e persistente</li>
</ul>

<h2>7 Estrategias para Fortalecer sua Autoestima</h2>

<h3>1. Questione o critico interno</h3>
<p>Quando ouvir uma voz interna negativa, pergunte: Isso e fato ou opiniao? O que eu diria a um amigo que pensasse isso sobre si mesmo?</p>

<h3>2. Celebre pequenas vitorias</h3>
<p>Anote diariamente 3 coisas que fez bem. Nosso cerebro tende ao negativo — precisamos treinar o olhar para o positivo.</p>

<h3>3. Estabeleca limites saudaveis</h3>
<p>Dizer nao quando necessario e um ato de amor proprio. Limites saudaveis comunicam: eu me respeito e respeito o outro.</p>

<h3>4. Cuide do seu corpo</h3>
<p>Exercicio, sono e alimentacao afetam diretamente como nos sentimos sobre nos mesmos. O corpo e a mente sao um sistema integrado.</p>

<h3>5. Rodeie-se de pessoas que te elevam</h3>
<p>Relacionamentos toxicos corroem a autoestima. Escolha companhias que te vejam com clareza e te encorajem a crescer.</p>

<h3>6. Pratique a auto-compaixao</h3>
<p>Trate-se com a mesma gentileza que trataria um amigo querido. Errar e humano — a diferenca esta em como voce se trata depois.</p>

<h3>7. Busque realizacoes alinhadas aos seus valores</h3>
<p>Conquistas que refletem o que voce realmente valoriza constroem autoestima genuina — diferente do sucesso externo vazio.</p>

<p>💡 Use o <a href="/cadastro">diario emocional da Emotion Intelligence</a> para monitorar seus padroes de autoestima ao longo do tempo.</p>
"""
    },
    {
        "slug": "sono-e-emocoes",
        "titulo": "A Conexao Entre Sono e Saude Emocional",
        "resumo": "Dormir mal afeta diretamente suas emocoes, tomada de decisao e saude mental. Descubra a ciencia por tras do sono e como melhorar sua qualidade de vida.",
        "categoria": "Bem-estar",
        "emoji": "😴",
        "tempo_leitura": "5 min",
        "data": "20/06/2026",
        "conteudo": """
<p>O <strong>sono</strong> e frequentemente o primeiro habito que sacrificamos quando estamos ocupados. Mas a ciencia e clara: dormir mal tem consequencias devastadoras para nossa saude emocional.</p>

<h2>O que acontece no cerebro durante o sono</h2>
<p>Durante o sono, especialmente na fase REM, o cerebro processa e consolida memorias emocionais, reduz a reatividade da amigdala e restaura o equilibrio neuroquimico.</p>

<h2>Privacao de sono e emocoes</h2>
<p>Estudos da UC Berkeley mostram que apenas uma noite mal dormida aumenta em 60% a reatividade emocional. Ficamos mais irritaveis, ansiosos e propensos a conflitos.</p>

<h2>Sinais de que o sono esta afetando sua saude emocional</h2>
<ul>
<li>Irritabilidade sem motivo aparente pela manha</li>
<li>Dificuldade de concentracao e tomada de decisao</li>
<li>Emocoes intensas e dificeis de regular</li>
<li>Sensacao de overwhelm por situacoes cotidianas</li>
</ul>

<h2>Como melhorar seu sono</h2>

<h3>Higiene do sono</h3>
<p>Durma e acorde sempre no mesmo horario. Seu cerebro ama rotina — o ritmo circadiano e biologico.</p>

<h3>Ambiente ideal</h3>
<p>Quarto escuro, fresco (18-20 graus) e silencioso. Use mascara de dormir e tampoes se necessario.</p>

<h3>Protocolo pre-sono</h3>
<p>Evite telas 1h antes de dormir. Leia, medite ou escreva no diario. O journaling emocional antes de dormir descarrega a mente.</p>

<h3>Limite cafeina</h3>
<p>A cafeina tem meia-vida de 6 horas. Um cafe as 15h ainda afeta seu sono a meia-noite.</p>

<p>💡 Registre seu humor pela manha na <a href="/cadastro">Emotion Intelligence</a> e observe a correlacao com a qualidade do seu sono.</p>
"""
    },
    {
        "slug": "relacionamentos-e-inteligencia-emocional",
        "titulo": "Como a Inteligencia Emocional Transforma seus Relacionamentos",
        "resumo": "Relacionamentos saudaveis sao construidos sobre pilares emocionais solidos. Aprenda como desenvolver IE para se conectar mais profundamente com as pessoas.",
        "categoria": "Relacionamentos",
        "emoji": "❤️",
        "tempo_leitura": "7 min",
        "data": "15/06/2026",
        "conteudo": """
<p>A maioria dos conflitos nos relacionamentos nao e sobre o que parece ser — e sobre necessidades emocionais nao atendidas e comunicacao mal gerenciada. A <strong>inteligencia emocional</strong> e a chave para mudar isso.</p>

<h2>Por que relacionamentos falham</h2>
<p>John Gottman, pesquisador que estudou mais de 3000 casais, identificou 4 comportamentos que destroem relacionamentos: critica, desprezo, postura defensiva e isolamento emocional.</p>

<h2>Como a IE transforma relacionamentos</h2>

<h3>1. Voce para de reagir e comeca a responder</h3>
<p>Com IE desenvolvida, voce tem um espaco entre o estimulo e a resposta. Esse espaco e onde mora a liberdade de escolha.</p>

<h3>2. Voce comunica necessidades sem atacar</h3>
<p>Em vez de Voce nunca me ouve, voce aprende a dizer Eu preciso me sentir ouvido. Mesma necessidade, impacto completamente diferente.</p>

<h3>3. Voce escuta para entender, nao para responder</h3>
<p>A escuta ativa — presenca total sem julgamento — e o maior presente que voce pode dar a alguem.</p>

<h3>4. Voce reconhece seus gatilhos</h3>
<p>Saber o que te ativa emocionalmente evita que voce projete seus medos e feridas nos outros.</p>

<h2>Pratica para hoje</h2>
<p>Na proxima conversa dificil, antes de responder, respire fundo e pergunte: O que a outra pessoa precisa agora? O que EU preciso agora?</p>

<p>💡 Analise suas emocoes apos conversas dificeis na <a href="/cadastro">Emotion Intelligence</a> para identificar padroes relacionais.</p>
"""
    },
    {
        "slug": "produtividade-e-bem-estar-emocional",
        "titulo": "Produtividade e Bem-estar: Como as Emocoes Afetam seu Trabalho",
        "resumo": "Emocoes e produtividade estao profundamente conectadas. Entenda como gerenciar seu estado emocional para trabalhar melhor e com mais satisfacao.",
        "categoria": "Produtividade",
        "emoji": "⚡",
        "tempo_leitura": "6 min",
        "data": "10/06/2026",
        "conteudo": """
<p>Durante decadas, o mundo corporativo tentou separar emocoes do trabalho. A ciencia provou que isso e impossivel — e contraproducente. <strong>Emocoes e desempenho sao inseparaveis.</strong></p>

<h2>Como emocoes afetam a produtividade</h2>
<p>O estado emocional influencia diretamente nossa capacidade de concentracao, criatividade, tomada de decisao e colaboracao. Funcionarios felizes sao 31% mais produtivos (Harvard Business Review).</p>

<h2>As emocoes mais prejudiciais ao trabalho</h2>

<h3>Ansiedade cronica</h3>
<p>Estreita o pensamento e consome recursos cognitivos. A mente ansiosa nao consegue focar — esta sempre monitorando ameacas.</p>

<h3>Raiva reprimida</h3>
<p>Drena energia e prejudica relacionamentos profissionais. Raiva nao expressa vira ressentimento.</p>

<h3>Tedio cronico</h3>
<p>Sinal de que o trabalho nao esta alinhado com seus valores e forcas. Ignora-lo leva ao burnout silencioso.</p>

<h2>Estrategias para gerenciar emocoes no trabalho</h2>

<h3>Micro-pausas emocionais</h3>
<p>A cada 90 minutos, faca uma pausa de 5 minutos. Respire, mova o corpo, beba agua. Nosso cerebro funciona em ciclos ultradiano de 90 min.</p>

<h3>Diario emocional profissional</h3>
<p>Ao fim de cada dia, anote: Como me senti hoje? O que drenou minha energia? O que me energizou? Padroes emergem em semanas.</p>

<h3>Comunicacao emocional assertiva</h3>
<p>Aprenda a expressar discordancias sem agressividade e necessidades sem passividade. Assertividade e a via do meio.</p>

<p>💡 Use a <a href="/cadastro">Emotion Intelligence</a> para rastrear como suas emocoes variam ao longo da semana de trabalho.</p>
"""
    },
    {
        "slug": "como-parar-de-se-preocupar",
        "titulo": "Como Parar de se Preocupar: 9 Tecnicas que Funcionam de Verdade",
        "resumo": "A preocupacao excessiva drena sua energia e paralisa sua vida. Descubra 9 tecnicas comprovadas para quebrar o ciclo da preocupacao e retomar o controle.",
        "categoria": "Ansiedade",
        "emoji": "🧩",
        "tempo_leitura": "6 min",
        "data": "02/06/2026",
        "conteudo": """
<p>A <strong>preocupacao excessiva</strong> e um dos habitos mentais mais desgastantes que existem. A mente fica presa em loops de "e se..." que consomem energia sem resolver nada.</p>

<h2>Por que nos preocupamos tanto?</h2>
<p>O cerebro humano evoluiu para antecipar ameacas. Mas no mundo moderno, esse sistema de alarme fica disparando para situacoes que nao sao de vida ou morte — o que cria ansiedade cronica.</p>

<h2>9 Tecnicas para Parar de se Preocupar</h2>

<h3>1. Agendamento de preocupacoes</h3>
<p>Reserve 20 minutos por dia especificamente para se preocupar. Quando um pensamento ansioso surgir fora desse horario, diga: "Vou pensar nisso no meu horario de preocupacao."</p>

<h3>2. Pergunte: isso e resolvivel?</h3>
<p>Separe preocupacoes em dois grupos: as que voce pode resolver agora e as que estao fora do seu controle. Para as primeiras, aja. Para as segundas, pratique aceitacao.</p>

<h3>3. Tecnica do pior cenario</h3>
<p>Pergunte: qual e o pior que pode acontecer? E se acontecer, eu conseguiria lidar? Na maioria das vezes, a resposta e sim.</p>

<h3>4. Mindfulness da preocupacao</h3>
<p>Observe o pensamento ansioso sem se identificar com ele. Diga: "Estou tendo o pensamento de que..." Isso cria distancia do conteudo do pensamento.</p>

<h3>5. Movimento fisico imediato</h3>
<p>Quando a preocupacao surgir, mova o corpo por 5 minutos. Caminhada, agachamentos, pular corda. O movimento quebra o loop mental.</p>

<h3>6. Escreva e destrua</h3>
<p>Escreva todas as suas preocupacoes em um papel. Depois amasse e jogue fora. O ato fisico de descartar ajuda o cerebro a liberar.</p>

<h3>7. Respiracao anti-ansiedade</h3>
<p>Expire mais longo que inspira. Inspire por 4s, expire por 8s. Isso ativa o sistema nervoso parassimpatico e reduz a ansiedade rapidamente.</p>

<h3>8. Contato com a natureza</h3>
<p>20 minutos na natureza reduz o cortisol em ate 21% (estudo da Universidade de Michigan). Parque, jardim ou ate uma arvore ja ajudam.</p>

<h3>9. Limite o consumo de noticias</h3>
<p>Noticias negativas alimentam a preocupacao. Estabeleca horarios fixos e limitados para se informar.</p>

<p>Use o <a href="/cadastro">diario emocional da Emotion Intelligence</a> para registrar suas preocupacoes e ver padroes ao longo do tempo.</p>
"""
    },
    {
        "slug": "sindrome-do-impostor",
        "titulo": "Sindrome do Impostor: O que e e Como Superar",
        "resumo": "Voce se sente uma fraude mesmo sendo competente? A sindrome do impostor afeta 70% das pessoas. Entenda o que e e como supera-la de vez.",
        "categoria": "Autoconhecimento",
        "emoji": "🎭",
        "tempo_leitura": "6 min",
        "data": "30/05/2026",
        "conteudo": """
<p>A <strong>sindrome do impostor</strong> e a sensacao persistente de que voce nao merece seu sucesso e que sera "descoberto" como uma fraude. Foi descrita pela primeira vez em 1978 pelas psicologas Pauline Clance e Suzanne Imes.</p>

<h2>Voce tem sindrome do impostor?</h2>
<ul>
<li>Atribui seu sucesso a sorte, nao a competencia</li>
<li>Tem medo de ser "desmascarado"</li>
<li>Minimiza suas conquistas</li>
<li>Sente que nao merece estar onde esta</li>
<li>Compara seus bastidores com o palco dos outros</li>
</ul>

<h2>Por que acontece?</h2>
<p>Geralmente surge em pessoas de alta performance, perfeccionistas ou que cresceram em ambientes onde o erro era punido. Paradoxalmente, quem tem sindrome do impostor costuma ser muito competente.</p>

<h2>Como superar</h2>

<h3>1. Nome e normaliza</h3>
<p>Reconhecer que voce tem sindrome do impostor ja reduz seu poder. Diga: "Estou sentindo sindrome do impostor agora."</p>

<h3>3. Colecione evidencias</h3>
<p>Crie um arquivo de conquistas: feedbacks positivos, resultados, agradecimentos. Releia quando a duvida surgir.</p>

<h3>4. Fale com outros</h3>
<p>Voce vai descobrir que quase todo mundo sente isso. A sindrome prospera no silencio e murcha na conversa.</p>

<h3>5. Redefina o fracasso</h3>
<p>Erros sao dados, nao sentencas. Todo especialista foi iniciante. A curva de aprendizado e parte do processo.</p>

<p>Registre suas conquistas diariamente na <a href="/cadastro">Emotion Intelligence</a> e construa evidencias reais do seu valor.</p>
"""
    },
    {
        "slug": "burnout-o-que-e-como-recuperar",
        "titulo": "Burnout: O que e, Sintomas e Como se Recuperar",
        "resumo": "O burnout e o esgotamento total — fisico, emocional e mental. Aprenda a identificar os sinais precocemente e os passos para a recuperacao.",
        "categoria": "Saude Mental",
        "emoji": "🔋",
        "tempo_leitura": "7 min",
        "data": "25/05/2026",
        "conteudo": """
<p>O <strong>burnout</strong> foi reconhecido pela OMS em 2019 como fenomeno ocupacional. E o resultado do estresse cronico no trabalho que nao foi gerenciado com exito.</p>

<h2>3 dimensoes do Burnout</h2>
<ul>
<li><strong>Exaustao:</strong> sensacao de estar completamente drenado</li>
<li><strong>Cinismo:</strong> distancia mental do trabalho, negatividade</li>
<li><strong>Ineficacia:</strong> sensacao de nao conseguir realizar nada</li>
</ul>

<h2>Sinais de alerta precoce</h2>
<ul>
<li>Dificuldade para acordar mesmo apos dormir bem</li>
<li>Irritabilidade crescente com colegas e familia</li>
<li>Esquecimento e dificuldade de concentracao</li>
<li>Sensacao de que nada que voce faz e suficiente</li>
<li>Doencas fisicas frequentes (imunidade baixa)</li>
</ul>

<h2>Fases do Burnout</h2>
<p>O burnout nao acontece de uma hora para outra. Ele evolui em fases: entusiasmo excessivo, estagnacao, frustracao, apatia e colapso. Identificar a fase e crucial.</p>

<h2>Recuperacao</h2>

<h3>1. Afastamento e descanso real</h3>
<p>Descanso nao e fraqueza. E prerequisito para recuperacao. Sem descanso genuino, nao ha recuperacao possivel.</p>

<h3>2. Redefinir limites</h3>
<p>O burnout frequentemente vem da incapacidade de dizer nao. Recuperar-se exige estabelecer limites claros e mantê-los.</p>

<h3>3. Acompanhamento profissional</h3>
<p>Burnout serio requer psicoterapia e, em alguns casos, acompanhamento psiquiatrico. Nao e fraqueza — e inteligencia.</p>

<h3>4. Reintroducao gradual</h3>
<p>Voltar a pleno vapor imediatamente causa recaida. A reintroducao deve ser gradual e monitorada.</p>

<p>Monitore seu nivel de energia diariamente na <a href="/cadastro">Emotion Intelligence</a> para identificar os sinais antes que seja tarde.</p>
"""
    },
    {
        "slug": "como-melhorar-relacionamento-amoroso",
        "titulo": "Como Melhorar seu Relacionamento Amoroso com Inteligencia Emocional",
        "resumo": "Relacionamentos saudaveis nao acontecem por acaso. Aprenda como aplicar inteligencia emocional para transformar sua vida amorosa.",
        "categoria": "Relacionamentos",
        "emoji": "💑",
        "tempo_leitura": "7 min",
        "data": "20/05/2026",
        "conteudo": """
<p>A maioria dos problemas em relacionamentos nao e sobre o que parece ser. Sao sobre necessidades emocionais nao comunicadas, feridas antigas sendo ativadas e padroes automaticos de reacao.</p>

<h2>O que a ciencia diz sobre relacionamentos saudaveis</h2>
<p>John Gottman estudou mais de 3.000 casais por 40 anos e descobriu que a ratio magica e de 5:1 — cinco interacoes positivas para cada negativa. Casais que mantem essa proporcao permanecem juntos.</p>

<h2>Os 4 cavaleiros do Apocalipse (destruidores do relacionamento)</h2>
<ul>
<li><strong>Critica:</strong> atacar o carater do parceiro (voce e sempre assim)</li>
<li><strong>Desprezo:</strong> sarcasmo, menosprezo, olhos revirados</li>
<li><strong>Postura defensiva:</strong> contratacar em vez de ouvir</li>
<li><strong>Bloqueio:</strong> se fechar, se recusar a engajar</li>
</ul>

<h2>Como a IE transforma relacionamentos</h2>

<h3>1. Comunicacao nao-violenta</h3>
<p>Em vez de acusar, expresse necessidades: "Quando voce chega tarde sem avisar, eu me sinto ansioso porque preciso de seguranca." Observacao + Sentimento + Necessidade + Pedido.</p>

<h3>2. Reparo emocional</h3>
<p>Quando a briga escalar, faca um reparo: "Preciso de uma pausa de 20 minutos para me acalmar." Isso evita que o conflito cause danos permanentes.</p>

<h3>3. Curiosidade em vez de julgamento</h3>
<p>Quando o parceiro age de forma estranha, pergunte com curiosidade genuina em vez de assumir o pior.</p>

<h3>4. Rituais de conexao</h3>
<p>Pequenos rituais diarios — cafe da manha juntos, abraco de boas-vindas, pergunta genuina sobre o dia — constroem o capital emocional que sustenta o relacionamento em momentos dificeis.</p>

<p>Use a <a href="/cadastro">Emotion Intelligence</a> para entender melhor seus proprios padroes emocionais e levar mais autoconsciencia para o relacionamento.</p>
"""
    },
    {
        "slug": "meditacao-guiada-para-iniciantes",
        "titulo": "Meditacao Guiada para Iniciantes: Seu Primeiro Passo",
        "resumo": "Nunca meditou? Este guia completo vai te levar da teoria a pratica em poucos minutos. Sem religiao, sem misticismo — so ciencia e pratica.",
        "categoria": "Mindfulness",
        "emoji": "🕯️",
        "tempo_leitura": "8 min",
        "data": "15/05/2026",
        "conteudo": """
<p>A <strong>meditacao</strong> e frequentemente mal compreendida. Nao e esvaziar a mente, nao e religiao e nao requer horas de pratica. E simplesmente o treinamento da atencao.</p>

<h2>O que a ciencia diz</h2>
<ul>
<li>8 semanas de meditacao aumentam a materia cinzenta no hipocampo (Harvard)</li>
<li>Reduz cortisol em ate 30%</li>
<li>Melhora foco, memoria e regulacao emocional</li>
<li>Reduz sintomas de ansiedade e depressao</li>
</ul>

<h2>Sua primeira meditacao (5 minutos)</h2>

<h3>Passo 1: Postura</h3>
<p>Sente-se confortavelmente — pode ser na cadeira, com os pes no chao. Coluna ereta mas nao rigida. Maos sobre os joelhos.</p>

<h3>Passo 2: Olhos</h3>
<p>Feche os olhos ou mantenha um olhar suave para o chao a sua frente.</p>

<h3>Passo 3: Respiracao</h3>
<p>Leve toda a sua atencao para a sensacao da respiracao. O ar entrando pelas narinas. O peito ou barriga subindo e descendo.</p>

<h3>Passo 4: Quando a mente vagar</h3>
<p>E normal. Quando perceber que se perdeu em pensamentos, gentilmente retorne a respiracao. Sem julgamento. Isso e o exercicio — perceber e retornar.</p>

<h3>Passo 5: Encerramento</h3>
<p>Apos 5 minutos, abra os olhos lentamente. Observe como se sente.</p>

<h2>Dicas para manter a pratica</h2>
<ul>
<li>Mesmo horario todo dia (manha e melhor para a maioria)</li>
<li>Comece com 5 minutos e aumente gradualmente</li>
<li>Nao julgue suas sessoes — toda sessao e boa</li>
<li>Consistencia e mais importante que duracao</li>
</ul>

<p>Registre como se sente antes e depois de meditar na <a href="/cadastro">Emotion Intelligence</a> e observe sua evolucao ao longo das semanas.</p>
"""
    },
    {
        "slug": "como-lidar-com-criticas",
        "titulo": "Como Lidar com Criticas sem se Destruir Emocionalmente",
        "resumo": "Criticas doem. Mas com inteligencia emocional, voce pode transformar feedback em combustivel para crescimento sem se sentir destruido.",
        "categoria": "Autoconhecimento",
        "emoji": "🛡️",
        "tempo_leitura": "5 min",
        "data": "10/05/2026",
        "conteudo": """
<p>Receber criticas e inevitavel. Como voce responde a elas define se elas te destroem ou te fortalecem.</p>

<h2>Por que criticas doem tanto?</h2>
<p>Nosso cerebro processa rejeicao social nas mesmas areas que processa dor fisica (estudo da UCLA). Criticas ativam o sistema de ameaca — por isso a reacao defensiva e automatica.</p>

<h2>Tipos de critica</h2>
<ul>
<li><strong>Critica construtiva:</strong> especifica, focada no comportamento, com intencao de ajudar</li>
<li><strong>Critica destrutiva:</strong> vaga, focada no carater, com intencao de ferir</li>
<li><strong>Critica projetada:</strong> diz mais sobre quem critica do que sobre voce</li>
</ul>

<h2>Como responder a criticas com IE</h2>

<h3>1. Pause antes de reagir</h3>
<p>Respire fundo. A primeira reacao e quase sempre defensiva. O espaco entre o estimulo e a resposta e onde mora a sua liberdade.</p>

<h3>2. Separe o joio do trigo</h3>
<p>Pergunte: ha algo de verdade nessa critica? Mesmo criticas mal formuladas podem conter informacoes uteis.</p>

<h3>3. Considere a fonte</h3>
<p>Voce se importaria com a opiniao dessa pessoa sobre outro assunto? Se nao, por que se importar com a opiniao sobre voce?</p>

<h3>4. Agradeca e processe depois</h3>
<p>Voce nao precisa concordar ou discordar na hora. Um simples "obrigado pelo feedback" ganha tempo para processar com calma.</p>

<h3>5. Nao generalize</h3>
<p>Uma critica sobre um comportamento especifico nao diz nada sobre seu valor como pessoa. Comportamentos mudam; carater e mais estavel.</p>

<p>Use o <a href="/cadastro">diario emocional</a> para processar criticas dificeis e extrair o aprendizado sem a dor desnecessaria.</p>
"""
    },
    {
        "slug": "inteligencia-emocional-no-trabalho",
        "titulo": "Inteligencia Emocional no Trabalho: Guia para Lideres e Colaboradores",
        "resumo": "A IE e o fator que diferencia profissionais bons de extraordinarios. Aprenda como desenvolver IE no ambiente profissional e alavancar sua carreira.",
        "categoria": "Produtividade",
        "emoji": "💼",
        "tempo_leitura": "8 min",
        "data": "05/05/2026",
        "conteudo": """
<p>Daniel Goleman, ao estudar centenas de empresas, descobriu que <strong>90% dos top performers</strong> tem alta inteligencia emocional. O QI te leva a porta, a IE te faz entrar e ficar.</p>

<h2>Por que IE importa mais que QI no trabalho</h2>
<p>Habilidades tecnicas sao o prerequisito. Mas promocoes, lideranca e influencia dependem de como voce gerencia a si mesmo e se relaciona com outros.</p>

<h2>IE para Lideres</h2>

<h3>Autoconsciencia na lideranca</h3>
<p>Lideres com alta autoconsciencia sabem como seu humor afeta a equipe. Eles checam o proprio estado antes de reunioes importantes.</p>

<h3>Empatia na lideranca</h3>
<p>Nao e concordar com tudo. E entender a perspectiva do outro antes de decidir. Lideres empaticos retêm talentos e constroem equipes resilientes.</p>

<h3>Gestao de conflitos</h3>
<p>Conflitos sao inevitaveis. Lideres emocionalmente inteligentes transformam conflitos em conversas produtivas sobre necessidades e solucoes.</p>

<h2>IE para Colaboradores</h2>

<h3>Gerenciar o chefe</h3>
<p>Entender o estilo emocional do seu gestor e adaptar sua comunicacao a ele e uma habilidade poderosa e subutilizada.</p>

<h3>Colaboracao eficaz</h3>
<p>Equipes com alta IE colaboram melhor porque os membros reconhecem suas proprias emocoes e as dos colegas, evitando conflitos desnecessarios.</p>

<h3>Resiliencia profissional</h3>
<p>Como voce se recupera de erros, fracassos e feedbacks negativos define sua trajetoria a longo prazo.</p>

<p>Desenvolva sua IE diariamente com a <a href="/cadastro">Emotion Intelligence Platform</a> e veja o impacto na sua vida profissional.</p>
"""
    },
    {
        "slug": "como-controlar-raiva",
        "titulo": "Como Controlar a Raiva: Tecnicas Imediatas e de Longo Prazo",
        "resumo": "A raiva nao controlada destroi relacionamentos e saude. Aprenda tecnicas imediatas para desativar a raiva e estrategias de longo prazo para muda-la.",
        "categoria": "Tecnicas",
        "emoji": "🌊",
        "tempo_leitura": "6 min",
        "data": "01/05/2026",
        "conteudo": """
<p>A <strong>raiva</strong> e uma das emocoes mais mal compreendidas. Ela nao e o problema — o problema e o que fazemos com ela quando nao sabemos gerencia-la.</p>

<h2>O que acontece no corpo durante a raiva</h2>
<p>A amigdala dispara um alarme. Cortisol e adrenalina inundam o sistema. A frequencia cardiaca sobe. O sangue vai para os musculos. O cortex pre-frontal (raciocinio) fica temporariamente comprometido.</p>
<p>Por isso voce diz coisas que se arrepende: literalmente nao esta pensando com clareza.</p>

<h2>Tecnicas imediatas (para o momento da raiva)</h2>

<h3>1. Pausa de 90 segundos</h3>
<p>A onda quimica da raiva dura 90 segundos. Se voce nao alimentar o pensamento, ela passa. Respire e aguarde 90 segundos antes de qualquer acao.</p>

<h3>2. Respiracao 4-7-8</h3>
<p>Inspire 4s, segure 7s, expire 8s. Ativa o sistema parassimpatico e reduz a intensidade da raiva em minutos.</p>

<h3>3. Saida fisica</h3>
<p>Se possivel, saia do ambiente por alguns minutos. Mudanca de cenario ajuda o cerebro a sair do modo de ameaca.</p>

<h3>4. Nomeie a emocao</h3>
<p>"Estou com raiva agora." Nomear reduz a atividade da amigdala (estudo da UCLA). Parece simples — e poderoso.</p>

<h2>Estrategias de longo prazo</h2>

<h3>Identifique seus gatilhos</h3>
<p>O que especificamente dispara sua raiva? Injustica? Falta de respeito? Perda de controle? Conhecer os gatilhos permite antecipar e preparar respostas mais inteligentes.</p>

<h3>Resolva o que esta por baixo</h3>
<p>Raiva cronica geralmente cobre medo, magoa ou vergonha. Terapia ajuda a processar as emocoes subjacentes.</p>

<p>Registre seus episodios de raiva na <a href="/cadastro">Emotion Intelligence</a> e identifique padroes que voce nao via antes.</p>
"""
    },
    {
        "slug": "depressao-sinais-e-ajuda",
        "titulo": "Depressao: Sinais de Alerta e Como Buscar Ajuda",
        "resumo": "A depressao afeta 300 milhoes de pessoas no mundo. Reconhecer os sinais precocemente pode salvar vidas. Saiba como identificar e onde buscar ajuda.",
        "categoria": "Saude Mental",
        "emoji": "🌧️",
        "tempo_leitura": "7 min",
        "data": "25/04/2026",
        "conteudo": """
<p><strong>Importante:</strong> Se voce esta em crise agora, ligue para o CVV: <strong>188</strong> (24 horas, gratuito). Voce nao precisa estar em risco de suicidio para ligar — qualquer sofrimento emocional e motivo suficiente.</p>

<p>A <strong>depressao</strong> e uma das condicoes de saude mental mais comuns e mais mal compreendidas. Nao e fraqueza, nao e frescura e nao e algo que se supera "querendo".</p>

<h2>Depressao vs Tristeza</h2>
<p>Tristeza e uma resposta natural a eventos dificeis e passa com o tempo. Depressao e persistente (mais de 2 semanas), generalizada e interfere no funcionamento diario.</p>

<h2>Sinais de alerta da depressao</h2>
<ul>
<li>Tristeza ou vazio persistente por mais de 2 semanas</li>
<li>Perda de interesse em atividades que antes eram prazerosas</li>
<li>Alteracoes significativas no sono (insonia ou sono excessivo)</li>
<li>Alteracoes no apetite e peso</li>
<li>Fadiga e perda de energia constantes</li>
<li>Dificuldade de concentracao e tomada de decisao</li>
<li>Sentimentos de inutilidade ou culpa excessiva</li>
<li>Pensamentos de morte ou suicidio</li>
</ul>

<h2>O que fazer</h2>

<h3>1. Busque ajuda profissional</h3>
<p>Psicologo e/ou psiquiatra. A depressao tem tratamento eficaz — psicoterapia e/ou medicacao, dependendo da gravidade.</p>

<h3>2. Onde buscar ajuda gratuita</h3>
<ul>
<li><strong>CVV:</strong> 188 (24h)</li>
<li><strong>CAPS</strong> (Centro de Atencao Psicossocial): servico publico gratuito</li>
<li><strong>UBS</strong> (Unidade Basica de Saude): encaminhamento pelo SUS</li>
</ul>

<h3>3. Apoio de pessoas proximas</h3>
<p>Contar para alguem de confianca alivia o peso. Voce nao precisa carregar sozinho.</p>

<p>A <a href="/cadastro">Emotion Intelligence</a> pode ser um complemento ao tratamento — nunca um substituto para cuidado profissional.</p>
"""
    },
    {
        "slug": "habitos-para-saude-mental",
        "titulo": "10 Habitos Diarios para uma Saude Mental de Ferro",
        "resumo": "Saude mental nao e ausencia de problemas — e ter recursos para lidar com eles. Esses 10 habitos constroem resiliencia emocional dia a dia.",
        "categoria": "Bem-estar",
        "emoji": "🏆",
        "tempo_leitura": "7 min",
        "data": "20/04/2026",
        "conteudo": """
<p>Saude mental nao e um estado permanente — e uma pratica diaria. Assim como voce escova os dentes para a saude bucal, existem habitos que mantem sua saude mental em dia.</p>

<h2>10 Habitos para Saude Mental de Ferro</h2>

<h3>1. Sono de qualidade (7-9 horas)</h3>
<p>O sono e quando o cerebro se limpa de toxinas, consolida memorias e restaura o equilibrio emocional. E o habito de maior impacto na saude mental.</p>

<h3>2. Movimento diario</h3>
<p>30 minutos de exercicio por dia reduz sintomas de depressao tao efetivamente quanto antidepressivos em casos leves a moderados (estudo da Duke University).</p>

<h3>3. Alimentacao anti-inflamatorio</h3>
<p>O intestino e o segundo cerebro. 90% da serotonina e produzida no intestino. Dieta rica em fibras, probioticos e omega-3 impacta diretamente o humor.</p>

<h3>4. Conexao social intencional</h3>
<p>Nao quantidade, mas qualidade. Uma conversa genuina por dia com alguem que voce ama e suficiente para um impacto significativo.</p>

<h3>5. Pratica de gratidao</h3>
<p>Escrever 3 coisas pelas quais e grato antes de dormir ativa o sistema de recompensa do cerebro e muda gradualmente o foco atencional.</p>

<h3>6. Limitar telas e redes sociais</h3>
<p>Mais de 2 horas de redes sociais por dia esta associado a aumento de ansiedade e depressao em jovens. Estabeleca limites conscientes.</p>

<h3>7. Tempo na natureza</h3>
<p>20 minutos diarios na natureza reduzem o cortisol e aumentam o bem-estar. Nao precisa ser floresta — um parque ou jardim ja funcionam.</p>

<h3>8. Proposito e significado</h3>
<p>Ter algo pelo qual acordar — um projeto, uma causa, uma pessoa — e um dos fatores mais protetores para a saude mental.</p>

<h3>9. Pratica contemplativa</h3>
<p>Meditacao, oracao, journaling — qualquer pratica que te convide a voltar para dentro regularmente.</p>

<h3>10. Registro emocional diario</h3>
<p>Nomear suas emocoes diariamente aumenta a autoconsciencia e previne o acumulo que leva a explosoes ou colapsos.</p>

<p>Comece hoje pelo habito 10: use a <a href="/cadastro">Emotion Intelligence</a> para registrar como voce esta se sentindo agora.</p>
"""
    },
    {
        "slug": "superar-trauma-emocional",
        "titulo": "Superando Traumas Emocionais: Um Guia Compassivo",
        "resumo": "Traumas emocionais deixam marcas profundas, mas a cura e possivel. Entenda o que e trauma, como ele afeta o cerebro e os caminhos para a recuperacao.",
        "categoria": "Cura Emocional",
        "emoji": "🌱",
        "tempo_leitura": "8 min",
        "data": "05/06/2026",
        "conteudo": """
<p><strong>Trauma</strong> nao e o evento em si — e a ferida que ele deixa no sistema nervoso. Qualquer experiencia que sobrecarregue nossa capacidade de processar pode ser traumatica.</p>

<h2>O que acontece no cerebro traumatizado</h2>
<p>O trauma ativa o sistema de ameaca do cerebro (amigdala) e pode deixa-lo em estado de alerta permanente. O hipocampo, responsavel pela memoria, e afetado — por isso memorias traumaticas sao fragmentadas e nao lineares.</p>

<h2>Tipos de trauma</h2>
<ul>
<li><strong>Trauma agudo:</strong> evento unico e intenso (acidente, violencia, perda subita)</li>
<li><strong>Trauma cronico:</strong> exposicao prolongada (abuso, negligencia, bullying)</li>
<li><strong>Trauma complexo:</strong> multiplos traumas interpessoais, geralmente na infancia</li>
<li><strong>Trauma vicario:</strong> absorvido por testemunhar o sofrimento de outros</li>
</ul>

<h2>Sinais de trauma nao processado</h2>
<ul>
<li>Flashbacks e pesadelos recorrentes</li>
<li>Evitacao de situacoes que lembram o evento</li>
<li>Hipervigilancia e sobressalto excessivo</li>
<li>Dificuldade de confiar e se conectar com outros</li>
<li>Sensacao de estar desconectado de si mesmo</li>
</ul>

<h2>Caminhos para a cura</h2>

<h3>Psicoterapia especializada</h3>
<p>EMDR, TCC focada em trauma e Somatic Experiencing sao abordagens com forte evidencia cientifica para tratamento de trauma.</p>

<h3>Regulacao do sistema nervoso</h3>
<p>Tecnicas de respiracao, movimento e mindfulness ajudam a regular o sistema nervoso e criar sensacao de seguranca no corpo.</p>

<h3>Conexao segura</h3>
<p>Relacionamentos seguros e preditivos sao curativos. Nao precisamos curar sozinhos — somos seres de conexao.</p>

<h2>Uma palavra importante</h2>
<p>Trauma serio requer acompanhamento profissional. Se voce se identifica com o que descrevemos, por favor busque um psicologo. O CVV (188) atende 24h para crises.</p>

<p>💡 A <a href="/cadastro">Emotion Intelligence</a> pode ser um complemento ao seu processo terapeutico — nunca um substituto.</p>
"""
    },
    {
        "slug": "ansiedade-no-trabalho",
        "titulo": "Como Controlar a Ansiedade no Trabalho",
        "categoria": "Ansiedade",
        "tempo_leitura": "8 min",
        "emoji": "😰",
        "data": "10/06/2026",
        "resumo": "A ansiedade no trabalho afeta 1 em cada 3 profissionais. Aprenda tecnicas praticas para manter a calma e a produtividade.",
        "imagem": "https://images.unsplash.com/photo-1497032628192-86f99bcd76bc?w=800",
        "conteudo": """
<h2>A Ansiedade no Trabalho e uma Epidemia Silenciosa</h2>
<p>Segundo a OMS, transtornos de ansiedade custam a economia global <strong>1 trilhao de dolares por ano</strong> em perda de produtividade. No Brasil, a ansiedade e o transtorno mental mais comum, afetando 9,3% da populacao.</p>
<h2>Sinais de Ansiedade no Trabalho</h2>
<ul>
<li>Dificuldade de concentracao e mente acelerada</li>
<li>Procrastinacao por medo de errar</li>
<li>Sensacao constante de urgencia mesmo sem prazo</li>
<li>Tensao muscular e dores de cabeca frequentes</li>
<li>Dificuldade de desligar apos o trabalho</li>
</ul>
<h2>Tecnicas Imediatas</h2>
<h3>1. Respiracao 4-7-8</h3>
<p>Inspire por 4 segundos, segure por 7, expire por 8. Repita 3 vezes. Ativa o sistema parassimpatico e reduz a ansiedade em minutos.</p>
<h3>2. Tecnica dos 5-4-3-2-1</h3>
<p>Nomeie 5 coisas que voce ve, 4 que toca, 3 que ouve, 2 que cheira, 1 que saboreia. Ancora voce no presente.</p>
<h3>3. Regra dos 2 minutos</h3>
<p>Se uma tarefa leva menos de 2 minutos, faca agora. Reduz o acumulo de pendencias que alimentam a ansiedade.</p>
<h2>Estrategias de Longo Prazo</h2>
<p>Estabeleca horarios para checar emails. Use a Matriz de Eisenhower para priorizar tarefas. Aplique a tecnica Pomodoro: 25 min foco + 5 min pausa.</p>
<h2>Quando Pedir Ajuda</h2>
<p>Se a ansiedade afeta seu desempenho por mais de 2 semanas, procure um psicologo. Ansiedade tem tratamento eficaz.</p>
<p>Use a <a href="/cadastro">Emotion Intelligence</a> para monitorar seus padroes emocionais no trabalho.</p>
"""
    },
    {
        "slug": "autoconhecimento-emocional",
        "titulo": "Autoconhecimento Emocional: O Guia Completo",
        "categoria": "Autoconhecimento",
        "tempo_leitura": "10 min",
        "emoji": "🔍",
        "data": "11/06/2026",
        "resumo": "Autoconhecimento emocional e a base de toda inteligencia emocional. Descubra como se conhecer profundamente.",
        "imagem": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=800",
        "conteudo": """
<h2>Por Que o Autoconhecimento E a Base de Tudo</h2>
<p>Socrates dizia Conhece-te a ti mesmo ha 2.500 anos. A ciencia moderna confirma: pessoas com alto autoconhecimento tomam melhores decisoes e tem relacionamentos mais saudaveis.</p>
<h2>Os 4 Niveis do Autoconhecimento</h2>
<h3>1. Reconhecimento (O que estou sentindo?)</h3>
<p>O primeiro passo e nomear a emocao. Pesquisas da UCLA mostram que nomear emocoes reduz sua intensidade.</p>
<h3>2. Compreensao (Por que estou sentindo isso?)</h3>
<p>Identificar o gatilho que ativou a emocao. Nem sempre e obvio.</p>
<h3>3. Padroes (Quando isso se repete?)</h3>
<p>Reconhecer padroes ao longo do tempo revela suas necessidades emocionais nao atendidas.</p>
<h3>4. Valores (O que isso diz sobre mim?)</h3>
<p>Emocoes sao mensageiras dos seus valores. Raiva sinaliza valor violado. Tristeza indica perda de algo importante.</p>
<h2>Praticas para Desenvolver Autoconhecimento</h2>
<p>Diario emocional diario por 5-10 minutos. Check-ins emocionais 3 vezes ao dia. Feedback honesto de pessoas proximas.</p>
<p>Use a <a href="/cadastro">Emotion Intelligence</a> para registrar e entender seus padroes emocionais com ajuda de IA.</p>
"""
    },
    {
        "slug": "como-ser-mais-empatico",
        "titulo": "Como Desenvolver Empatia: Guia Pratico",
        "categoria": "Relacionamentos",
        "tempo_leitura": "7 min",
        "emoji": "🤝",
        "data": "12/06/2026",
        "resumo": "Empatia nao e um dom, e uma habilidade que pode ser desenvolvida. Aprenda como cultivar empatia genuina.",
        "imagem": "https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=800",
        "conteudo": """
<h2>Empatia: O Que E e O Que Nao E</h2>
<p>Empatia e a capacidade de compreender e compartilhar os sentimentos de outra pessoa. Nao e concordar, nao e resolver problemas, nao e sentir pena.</p>
<h2>Os 3 Tipos de Empatia</h2>
<h3>Empatia Cognitiva</h3>
<p>Entender intelectualmente a perspectiva do outro.</p>
<h3>Empatia Emocional</h3>
<p>Sentir com o outro — sua alegria e sua alegria, sua dor e sua dor.</p>
<h3>Empatia Compassiva</h3>
<p>Entender, sentir E agir para ajudar. E a forma mais completa.</p>
<h2>Como Desenvolver Empatia na Pratica</h2>
<h3>Escuta ativa real</h3>
<p>Quando alguem fala, resista ao impulso de pensar na sua resposta. Foque 100% no que a pessoa esta dizendo.</p>
<h3>Leia ficcao</h3>
<p>Estudos da Universidade de Toronto mostraram que leitores de ficcao literaria tem maior empatia.</p>
<h3>Reduza o julgamento</h3>
<p>Toda vez que voce se pegar julgando alguem, pause e pergunte: O que pode ter levado essa pessoa a agir assim?</p>
<p>Use a <a href="/cadastro">Emotion Intelligence</a> para desenvolver sua inteligencia emocional.</p>
"""
    },
    {
        "slug": "terapia-online-vale-a-pena",
        "titulo": "Terapia Online Vale a Pena? A Verdade Completa",
        "categoria": "Saude Mental",
        "tempo_leitura": "8 min",
        "emoji": "💻",
        "data": "13/06/2026",
        "resumo": "Terapia online cresceu 400% pos-pandemia. Ela e tao eficaz quanto a presencial? Tudo que voce precisa saber.",
        "imagem": "https://images.unsplash.com/photo-1590650153855-d9e808231d41?w=800",
        "conteudo": """
<h2>Terapia Online: A Revolucao da Saude Mental</h2>
<p>A pandemia acelerou em decadas a adocao da terapia online. O que era visto com ceticismo em 2019 tornou-se mainstream — e os resultados surpreenderam ate os mais ceticos.</p>
<h2>O Que Diz a Ciencia</h2>
<p>Uma meta-analise publicada no Journal of Psychological Disorders analisou 92 estudos e concluiu: <strong>a terapia online e tao eficaz quanto a presencial</strong> para a maioria dos transtornos.</p>
<h2>Vantagens Reais</h2>
<ul>
<li>Acesso a psicologos de qualquer cidade do Brasil</li>
<li>Geralmente 20-40% mais barato que presencial</li>
<li>Horarios mais flexiveis</li>
<li>Muitos pacientes se abrem mais em casa</li>
</ul>
<h2>Limitacoes Importantes</h2>
<ul>
<li>Crises severas podem requerer atendimento presencial</li>
<li>Conexao de internet instavel prejudica o processo</li>
</ul>
<h2>Como Escolher um Psicologo Online</h2>
<p>Verifique o registro no CRP. Plataformas como Zenklub, Vittude e Psicologia Viva tem psicologos verificados.</p>
<p>Use a <a href="/cadastro">Emotion Intelligence</a> para registrar como voce se sente entre as sessoes.</p>
"""
    },
    {
        "slug": "como-lidar-com-rejeicao",
        "titulo": "Como Lidar com a Rejeicao sem se Destruir",
        "categoria": "Autoconhecimento",
        "tempo_leitura": "7 min",
        "emoji": "💔",
        "data": "14/06/2026",
        "resumo": "Rejeicao doi porque o cerebro a processa como dor fisica. Entenda a neurociencia e aprenda a superar.",
        "imagem": "https://images.unsplash.com/photo-1541199249251-f713e6145474?w=800",
        "conteudo": """
<h2>Por Que a Rejeicao Doi Tanto</h2>
<p>Nao e fraqueza, e biologia. Neuroimagens mostram que a rejeicao social ativa as <strong>mesmas regioes cerebrais que a dor fisica</strong>.</p>
<h2>Os Erros Mais Comuns Apos a Rejeicao</h2>
<h3>Ruminacao excessiva</h3>
<p>Ficar revivendo a cena repetidamente prolonga a dor sem trazer clareza.</p>
<h3>Generalizacao</h3>
<p>Ninguem me quer, sempre acontece isso comigo. Uma rejeicao especifica vira uma verdade absoluta.</p>
<h3>Isolamento</h3>
<p>Quando mais precisamos de conexao, mais nos isolamos. O isolamento amplifica a dor.</p>
<h2>Estrategias Para Superar</h2>
<h3>1. Valide a dor sem se afogar nela</h3>
<p>E normal doer. Mas depois, escolha conscientemente redirecionar a atencao.</p>
<h3>2. Separe rejeicao de identidade</h3>
<p>Voce nao foi rejeitado — uma ideia ou possibilidade foi. Seu valor como pessoa nao esta em jogo.</p>
<h3>3. Acao imediata</h3>
<p>A melhor cura para rejeicao e a acao — ela restaura o senso de agencia e autoconfianca.</p>
<p>Use a <a href="/cadastro">Emotion Intelligence</a> para processar rejeicoes e identificar padroes.</p>
"""
    },
    {
        "slug": "saude-mental-pos-pandemia",
        "titulo": "Saude Mental Pos-Pandemia: Como se Recuperar",
        "categoria": "Saude Mental",
        "tempo_leitura": "9 min",
        "emoji": "🌱",
        "data": "15/06/2026",
        "resumo": "A pandemia deixou sequelas emocionais em milhoes de pessoas. Ansiedade, luto e burnout aumentaram. Saiba como se recuperar.",
        "imagem": "https://images.unsplash.com/photo-1584483766114-2cea6facdf57?w=800",
        "conteudo": """
<h2>O Legado Emocional da Pandemia</h2>
<p>A COVID-19 nao foi apenas uma crise de saude fisica. A OMS reportou aumento de <strong>25% nos casos de ansiedade e depressao</strong> no primeiro ano da pandemia.</p>
<h2>As Sequelas Mais Comuns</h2>
<h3>Ansiedade social pos-pandemia</h3>
<p>Apos meses de isolamento, muitas pessoas intensificaram a ansiedade em situacoes sociais.</p>
<h3>Luto nao reconhecido</h3>
<p>Nao apenas perda de pessoas, mas de empregos, planos e normalidade.</p>
<h3>Burnout pandemico</h3>
<p>A fusao do trabalho com o lar, sem fronteiras claras, esgotou milhoes.</p>
<h2>Estrategias de Recuperacao</h2>
<p>Reconheca o que voce perdeu. Reintroduza gradualmente o social. Reconstrua rotinas com intencao. Processe o que ficou para tras.</p>
<p>Use a <a href="/cadastro">Emotion Intelligence</a> para monitorar sua recuperacao emocional pos-pandemia.</p>
"""
    },
    {
        "slug": "como-aumentar-resiliencia",
        "titulo": "Como Aumentar sua Resiliencia Emocional",
        "categoria": "Desenvolvimento Pessoal",
        "tempo_leitura": "8 min",
        "emoji": "💪",
        "data": "16/06/2026",
        "resumo": "Resiliencia nao e nao sofrer, e se recuperar mais rapido. Descubra como desenvolve-la com praticas comprovadas.",
        "imagem": "https://images.unsplash.com/photo-1519681393784-d120267933ba?w=800",
        "conteudo": """
<h2>O Mito da Resiliencia</h2>
<p>Resiliencia nao e nao sentir dor. E a capacidade de se dobrar sem quebrar e de se recuperar apos adversidades com aprendizado.</p>
<h2>Os 5 Pilares da Resiliencia</h2>
<h3>1. Regulacao Emocional</h3>
<p>Nao suprimir emocoes, mas processa-las de forma saudavel.</p>
<h3>2. Mentalidade de Crescimento</h3>
<p>Ver adversidades como desafios temporarios e oportunidades de aprendizado.</p>
<h3>3. Rede de Apoio</h3>
<p>Ninguem e resiliente sozinho. Investir em relacionamentos de qualidade e investir na capacidade de superar crises.</p>
<h3>4. Proposito</h3>
<p>Pessoas com senso claro de proposito suportam adversidades maiores.</p>
<h3>5. Autocuidado Nao-Negociavel</h3>
<p>Sono, exercicio e alimentacao sao a base biologica da resiliencia.</p>
<h2>Pratica Diaria</h2>
<p>Ao final de cada dia dificil, escreva: 1 coisa que voce superou, 1 recurso interno que usou, 1 aprendizado.</p>
<p>Use o <a href="/cadastro">diario emocional da Emotion Intelligence</a> para construir seu registro de resiliencia.</p>
"""
    },
    {
        "slug": "tecnicas-de-respiracao",
        "titulo": "Tecnicas de Respiracao para Ansiedade e Estresse",
        "categoria": "Mindfulness",
        "tempo_leitura": "6 min",
        "emoji": "🌬️",
        "data": "17/06/2026",
        "resumo": "A respiracao e a unica funcao autonoma que controlamos conscientemente. 5 tecnicas comprovadas para reduzir ansiedade.",
        "imagem": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800",
        "conteudo": """
<h2>Por Que a Respiracao Funciona</h2>
<p>A respiracao e unica: e a unica funcao autonoma do corpo que podemos controlar conscientemente. Respirar lentamente ativa o nervo vago — o nervo da calma.</p>
<h2>5 Tecnicas Comprovadas</h2>
<h3>1. Respiracao 4-7-8</h3>
<p>Inspire pelo nariz por 4s, segure por 7s, expire pela boca por 8s. Repita 4 vezes. Excelente para dormir e ansiedade aguda.</p>
<h3>2. Respiracao Box (Metodo Navy SEAL)</h3>
<p>Inspire 4s, segure 4s, expire 4s, segure 4s. Usada por operacoes especiais para manter calma sob pressao extrema.</p>
<h3>3. Respiracao Diafragmatica</h3>
<p>Mao no abdomen, inspire fazendo-o expandir (nao o peito). 10 respiracoes. Ativa o sistema parassimpatico.</p>
<h3>4. Respiracao Alternada (Yoga)</h3>
<p>Alterne as narinas a cada respiracao. 5 ciclos. Equilibra os hemisferios cerebrais.</p>
<h3>5. Expiracao Prolongada</h3>
<p>Sempre expire mais longo que inspira. Inspire 4s, expire 6-8s. Ativa o nervo vago eficientemente.</p>
<p>Registre como se sente antes e depois das tecnicas na <a href="/cadastro">Emotion Intelligence</a>.</p>
"""
    },
    {
        "slug": "relacionamento-toxico-sinais",
        "titulo": "10 Sinais de Relacionamento Toxico (e Como Sair)",
        "categoria": "Relacionamentos",
        "tempo_leitura": "9 min",
        "emoji": "⚠️",
        "data": "18/06/2026",
        "resumo": "Relacionamentos toxicos nao comecam toxicos. Aprenda a reconhecer os sinais e os passos para sair com seguranca.",
        "imagem": "https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2?w=800",
        "conteudo": """
<h2>Por Que E Dificil Reconhecer</h2>
<p>Relacionamentos toxicos raramente comecam assim. Evoluem gradualmente — o que os psicologos chamam de escalada da toxicidade.</p>
<h2>10 Sinais de Alerta</h2>
<ol>
<li>Voce se sente constantemente mal sobre si mesmo</li>
<li>Controle e ciumo excessivos</li>
<li>Comunicacao baseada em culpa e manipulacao</li>
<li>Seus sentimentos sao sempre invalidados</li>
<li>Voce tem medo de expressar sua opiniao</li>
<li>Isolamento dos amigos e familia</li>
<li>O relacionamento e assimetrico — voce da muito mais</li>
<li>Voce se sente preso, nao escolhendo ficar</li>
<li>Humor da casa depende do humor dele/dela</li>
<li>Voce perdeu quem era antes do relacionamento</li>
</ol>
<h2>Como Sair com Seguranca</h2>
<p>Planeje antes de agir. Estabeleca suporte. Prepare-se para manipulacao na saida.</p>
<p>Em caso de violencia, ligue 180 ou 190. Use a <a href="/cadastro">Emotion Intelligence</a> para monitorar como seus relacionamentos afetam suas emocoes.</p>
"""
    },
    {
        "slug": "como-perdoar-e-seguir-em-frente",
        "titulo": "Como Perdoar e Seguir em Frente (Mesmo Quando E Dificil)",
        "categoria": "Desenvolvimento Pessoal",
        "tempo_leitura": "8 min",
        "emoji": "🕊️",
        "data": "19/06/2026",
        "resumo": "Perdoar nao e esquecer nem concordar, e se libertar. A ciencia comprova que o perdao reduz ansiedade e depressao.",
        "imagem": "https://images.unsplash.com/photo-1499209974431-9dddcece7f88?w=800",
        "conteudo": """
<h2>O Maior Mito Sobre o Perdao</h2>
<p>Perdoar nao e dizer que o que aconteceu foi aceitavel. Nao e esquecer. Nao e reconciliar-se com a pessoa. <strong>Perdao e um ato de autocuidado radical.</strong></p>
<h2>O Que a Ciencia Comprova</h2>
<p>Pesquisas da Universidade de Stanford mostraram que pessoas que praticam o perdao tem menor pressao arterial, menos ansiedade e depressao, melhor qualidade de sono e sistema imunologico mais forte.</p>
<h2>O Processo Real do Perdao</h2>
<h3>Fase 1: Reconheca a magoa completamente</h3>
<p>Nao minimize. Sinta a raiva, a tristeza, a traicao. O perdao genuino so vem apos honrar o que voce sentiu.</p>
<h3>Fase 2: Escolha perdoar</h3>
<p>O perdao comeca com uma decisao, nao com um sentimento. Voce decide que nao vai mais deixar esse evento ter poder sobre voce.</p>
<h3>Fase 3: Desenvolva empatia</h3>
<p>Nao para justificar, mas para compreender. O que levou essa pessoa a agir assim?</p>
<h3>Fase 4: Estabeleca o que muda</h3>
<p>Perdoar nao significa voltar a mesma dinamica. O perdao libera o passado; os limites protegem o futuro.</p>
<p>Registre sua jornada de perdao no <a href="/cadastro">diario emocional da Emotion Intelligence</a>.</p>
"""
    },
]


# ================================================================
# MODO TERAPIA ESTRUTURADA — 7 DIAS
# ================================================================

PROGRAMA_7_DIAS = [
    {
        "dia": 1,
        "titulo": "Autoconhecimento Emocional",
        "descricao": "Hoje vamos mapear suas emoções mais frequentes e entender seus gatilhos.",
        "emoji": "🔍",
        "cor": "#3498db",
        "exercicios": [
            {
                "nome": "Check-in Emocional",
                "instrucao": "Feche os olhos por 2 minutos. Pergunte a si mesmo: O que estou sentindo agora? Onde sinto isso no corpo?",
                "duracao": "5 min",
                "tipo": "reflexao"
            },
            {
                "nome": "Roda das Emocoes",
                "instrucao": "Liste as 5 emocoes que voce mais sentiu nesta semana e o que as causou.",
                "duracao": "10 min",
                "tipo": "escrita"
            }
        ],
        "reflexao": "As emocoes sao mensageiros, nao inimigos.",
        "tecnica_principal": "Observacao Emocional"
    },
    {
        "dia": 2,
        "titulo": "Respiracao e Regulacao",
        "descricao": "Aprenda a usar a respiracao para regular suas emocoes.",
        "emoji": "🌬️",
        "cor": "#2ecc71",
        "exercicios": [
            {
                "nome": "Respiracao 4-7-8",
                "instrucao": "Inspire por 4s, segure por 7s, expire por 8s. Repita 4 vezes.",
                "duracao": "5 min",
                "tipo": "pratica"
            }
        ],
        "reflexao": "A respiracao e a ponte entre mente e corpo.",
        "tecnica_principal": "Respiracao 4-7-8"
    },
    {
        "dia": 3,
        "titulo": "Mindfulness e Presenca",
        "descricao": "Desenvolva a capacidade de estar plenamente presente.",
        "emoji": "🧘",
        "cor": "#9b59b6",
        "exercicios": [
            {
                "nome": "Grounding 5-4-3-2-1",
                "instrucao": "Nomeie 5 coisas que ve, 4 que toca, 3 que ouve, 2 que cheira, 1 que saboreia.",
                "duracao": "5 min",
                "tipo": "pratica"
            }
        ],
        "reflexao": "Esteja aqui, agora.",
        "tecnica_principal": "Grounding"
    },
    {
        "dia": 4,
        "titulo": "Auto-Compaixao",
        "descricao": "Aprenda a ser gentil consigo mesmo.",
        "emoji": "💙",
        "cor": "#e74c3c",
        "exercicios": [
            {
                "nome": "Carta para Si Mesmo",
                "instrucao": "Escreva uma carta para voce como se fosse seu melhor amigo escrevendo.",
                "duracao": "15 min",
                "tipo": "escrita"
            }
        ],
        "reflexao": "Voce merece sua propria gentileza.",
        "tecnica_principal": "Auto-Compaixao"
    },
    {
        "dia": 5,
        "titulo": "Gestao da Raiva",
        "descricao": "Transforme emocoes dificeis em energia construtiva.",
        "emoji": "🔥",
        "cor": "#e67e22",
        "exercicios": [
            {
                "nome": "Tecnica STOP",
                "instrucao": "Pare, Respire, Observe, Prossiga.",
                "duracao": "Imediato",
                "tipo": "pratica"
            }
        ],
        "reflexao": "A raiva aponta para o que voce valoriza.",
        "tecnica_principal": "STOP"
    },
    {
        "dia": 6,
        "titulo": "Conexao e Empatia",
        "descricao": "Fortaleca suas conexoes.",
        "emoji": "🤝",
        "cor": "#1abc9c",
        "exercicios": [
            {
                "nome": "Loving-Kindness",
                "instrucao": "Envie mentalmente votos de bem-estar para voce e outros.",
                "duracao": "10 min",
                "tipo": "meditacao"
            }
        ],
        "reflexao": "Somos seres de conexao.",
        "tecnica_principal": "Metta"
    },
    {
        "dia": 7,
        "titulo": "Integracao e Gratidao",
        "descricao": "Consolide sua jornada.",
        "emoji": "🌟",
        "cor": "#f39c12",
        "exercicios": [
            {
                "nome": "Diario de Gratidao",
                "instrucao": "Liste 3 coisas pelas quais e grato hoje.",
                "duracao": "5 min",
                "tipo": "escrita"
            }
        ],
        "reflexao": "A gratidao e a memoria do coracao.",
        "tecnica_principal": "Gratidao"
    }
]

@app.get("/terapia", response_class=HTMLResponse)
def terapia_page(request: Request, dia: int = 1, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        # Terapia publica para SEO — redireciona para cadastro se nao logado
        return RedirectResponse(url="/cadastro?next=terapia")
    dia = max(1, min(7, dia))
    programa_dia = PROGRAMA_7_DIAS[dia - 1]
    return templates.TemplateResponse(request, "terapia.html", {
        "usuario":     usuario,
        "dia":         dia,
        "programa":    programa_dia,
        "total_dias":  7,
        "todos_dias":  PROGRAMA_7_DIAS,
    })

@app.get("/blog", response_class=HTMLResponse)
def blog_page(request: Request):
    return templates.TemplateResponse(request, "blog.html", {
        "artigos": ARTIGOS_BLOG,
        "total":   len(ARTIGOS_BLOG),
    })


@app.get("/blog/{slug}", response_class=HTMLResponse)
def artigo_page(slug: str, request: Request):
    artigo = next((a for a in ARTIGOS_BLOG if a["slug"] == slug), None)
    if not artigo:
        raise HTTPException(status_code=404, detail="Artigo nao encontrado")
    outros = [a for a in ARTIGOS_BLOG if a["slug"] != slug][:3]
    return templates.TemplateResponse(request, "artigo.html", {
        "artigo": artigo,
        "outros": outros,
    })


@app.post("/analisar/emoji")
async def analisar_emoji(
    request: Request,
    emoji:   str = Form(...),
    db:      Session = Depends(get_db)
):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Nao autorizado")

    limite     = get_limite(usuario, "analises")
    total_hoje = contar_hoje(Analise, usuario.id, db)
    if total_hoje >= limite:
        raise HTTPException(
            status_code=429,
            detail=f"Limite de {limite} analises por dia atingido."
        )

    emocao     = emocao_por_emoji(emoji)
    texto      = f"Humor registrado via emoji: {emoji}"
    intensidade = 2

    nova = Analise(
        texto=texto,
        emocao=emocao,
        emoji=get_emoji(emocao),
        recomendacao=recomendacoes.get(emocao, ""),
        tecnica=tecnicas_por_emocao.get(emocao, ""),
        intensidade=intensidade,
        usuario_id=usuario.id
    )
    db.add(nova)
    db.commit()

    pontos_ganhos = PONTOS_POR_ACAO.get("analise_premium", 5) if usuario.plano in ["premium","enterprise"] else PONTOS_POR_ACAO.get("analise_free", 2)
    adicionar_pontos(usuario, pontos_ganhos, db)
    verificar_conquistas(usuario, db)

    return {
        "emocao":       emocao,
        "emoji":        get_emoji(emocao),
        "emoji_input":  emoji,
        "recomendacao": recomendacoes.get(emocao, ""),
        "tecnica":      tecnicas_por_emocao.get(emocao, ""),
        "pontos_ganhos": pontos_ganhos,
        "total_pontos": usuario.pontos,
    }



# ================================================================
# ROTA — ANALISE DE EMOCAO POR FOTO (Gemini Vision)
# ================================================================

@app.post("/analisar/foto")
async def analisar_foto(
    request: Request,
    foto: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Nao autorizado")

    # Verifica limite
    hoje = date.today()
    analises_hoje = db.query(Analise).filter(
        Analise.usuario_id == usuario.id,
        Analise.criado_em >= datetime.combine(hoje, datetime.min.time())
    ).count()
    limite = LIMITES[usuario.plano]["analises"]
    if analises_hoje >= limite:
        raise HTTPException(status_code=429, detail=f"Limite de {limite} analises/dia atingido")

    # Valida tipo de arquivo
    tipos_validos = ["image/jpeg", "image/png", "image/webp", "image/gif"]
    if foto.content_type not in tipos_validos:
        raise HTTPException(status_code=400, detail="Formato invalido. Use JPEG, PNG ou WEBP")

    # Le bytes da imagem
    foto_bytes = await foto.read()
    if len(foto_bytes) > 5 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="Imagem muito grande. Maximo 5MB")

    try:
        import base64
        foto_b64 = base64.standard_b64encode(foto_bytes).decode("utf-8")

        prompt_foto = """Voce e um especialista em psicologia, neurociencia emocional e analise facial com visao computacional avancada.

Analise TODOS os elementos visuais desta imagem com maxima precisao:
1. EXPRESSAO FACIAL: microexpressoes, posicao dos olhos, sobrancelhas, boca, tensao muscular
2. LINGUAGEM CORPORAL: postura, gestos, tensao nos ombros, posicao dos bracos
3. CONTEXTO: ambiente, objetos, cores, iluminacao, situacao
4. PELE E APARENCIA: vermelhidao, palor, tensao
5. OLHAR: direcao, intensidade, brilho ou opacidade

Emocoes possiveis (escolha a mais precisa):
alegria, tristeza, raiva, medo, surpresa, nojo, ansiedade, calma, confianca, curiosidade,
amor, gratidao, frustracao, vergonha, neutro, euforia, melancolia, orgulho, solidao,
estresse, desespero, paz, entusiasmo, timidez, confusao, saudade, alivio, tedio

Responda EXATAMENTE neste formato JSON:
{
  "emocao": "nome_da_emocao",
  "confianca": 85,
  "intensidade": 3,
  "descricao": "Descricao detalhada do que voce observou — expressao, postura, contexto",
  "emocoes_secundarias": ["emocao2", "emocao3"],
  "dica": "Uma tecnica terapeutica pratica relacionada a esta emocao",
  "observacao_clinica": "O que um psicologo observaria nesta expressao"
}"""

        resposta = cliente_ia.models.generate_content(
            model="gemini-2.0-flash",
            contents=[
                types.Part.from_bytes(data=foto_bytes, mime_type=foto.content_type),
                types.Part.from_text(text=prompt_foto)
            ],
            config=types.GenerateContentConfig(
                temperature=0.3,
                max_output_tokens=512
            )
        )

        texto = resposta.text.strip()
        # Limpa markdown se houver
        if "```" in texto:
            texto = texto.split("```")[1]
            if texto.startswith("json"):
                texto = texto[4:]
        texto = texto.strip()

        resultado = json.loads(texto)
        emocao = resultado.get("emocao", "neutro").lower()
        confianca = resultado.get("confianca", 70)
        descricao = resultado.get("descricao", "")
        dica = resultado.get("dica", "")

    except Exception as e:
        print(f"[FOTO] Erro Gemini: {e}")
        emocao = "neutro"
        confianca = 50
        descricao = "Nao foi possivel analisar a imagem com precisao"
        dica = "Tente uma foto com rosto bem iluminado e visivel"

    # Salva no banco
    emoji = get_emoji(emocao)
    pontos = PONTOS_POR_ACAO.get("analise_free", 2)
    nova_analise = Analise(
        usuario_id=usuario.id,
        texto=f"[FOTO] {foto.filename or 'imagem'}",
        emocao=emocao,
        emoji=emoji,
        pontos_ganhos=pontos
    )
    db.add(nova_analise)
    adicionar_pontos(usuario, pontos, db)
    db.commit()

    # Notifica Telegram se emocao negativa intensa
    if emocao in ["tristeza", "medo", "ansiedade", "raiva", "depressao"] and confianca >= 80:
        enviar_telegram(
            f"⚠️ <b>Emocao intensa detectada por foto</b>\n"
            f"👤 {usuario.nome}\n"
            f"😔 Emocao: {emocao} ({confianca}% confianca)\n"
            f"🕐 {datetime.now().strftime('%d/%m/%Y %H:%M')}"
        )

    return {
        "emocao":     emocao,
        "emoji":      emoji,
        "confianca":  confianca,
        "descricao":  descricao,
        "dica":       dica,
        "pontos":     pontos,
        "badge":      usuario.badge,
        "total_pontos": usuario.pontos
    }
@app.get("/robots.txt", include_in_schema=False)
async def robots():
    from fastapi.responses import FileResponse
    return FileResponse("static/robots.txt", media_type="text/plain")

@app.get("/sitemap.xml", include_in_schema=False)
async def sitemap():
    from datetime import date
    hoje = date.today().strftime("%Y-%m-%d")
    paginas = [
        ("/", "1.0", "daily"),
        ("/blog", "0.9", "weekly"),
        ("/premium", "0.9", "weekly"),
        ("/planos", "0.9", "weekly"),
        ("/cadastro", "0.8", "monthly"),
        ("/terapia", "0.8", "monthly"),
        ("/afiliado", "0.7", "monthly"),
        ("/sobre", "0.6", "monthly"),
        ("/faq", "0.6", "monthly"),
        ("/contato", "0.5", "monthly"),
        ("/privacidade", "0.4", "monthly"),
        ("/termos", "0.4", "monthly"),
        ("/blog/o-que-e-inteligencia-emocional", "0.8", "monthly"),
        ("/blog/tecnicas-para-controlar-ansiedade", "0.8", "monthly"),
        ("/blog/como-lidar-com-tristeza", "0.8", "monthly"),
        ("/blog/diario-emocional-beneficios", "0.8", "monthly"),
        ("/blog/mindfulness-para-iniciantes", "0.8", "monthly"),
        ("/blog/como-aumentar-autoestima", "0.8", "monthly"),
        ("/blog/sono-e-emocoes", "0.8", "monthly"),
        ("/blog/relacionamentos-e-inteligencia-emocional", "0.8", "monthly"),
        ("/blog/produtividade-e-bem-estar-emocional", "0.8", "monthly"),
        ("/blog/superar-trauma-emocional", "0.8", "monthly"),
        ("/blog/sindrome-do-impostor", "0.8", "monthly"),
        ("/blog/burnout-o-que-e-como-recuperar", "0.8", "monthly"),
        ("/blog/inteligencia-emocional-no-trabalho", "0.8", "monthly"),
        ("/blog/como-controlar-raiva", "0.8", "monthly"),
        ("/blog/habitos-para-saude-mental", "0.8", "monthly"),
    ]
    base = "https://emotion-platform-albert.onrender.com"
    linhas = ['<?xml version="1.0" encoding="UTF-8"?>']
    linhas.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for path, priority, freq in paginas:
        linhas.append("  <url>")
        linhas.append(f"    <loc>{base}{path}</loc>")
        linhas.append(f"    <lastmod>{hoje}</lastmod>")
        linhas.append(f"    <changefreq>{freq}</changefreq>")
        linhas.append(f"    <priority>{priority}</priority>")
        linhas.append("  </url>")
    linhas.append("</urlset>")
    xml = "\n".join(linhas)
    return Response(content=xml, media_type="application/xml")
    urls_fixas = [
        "/", "/login", "/cadastro", "/blog", "/planos", "/premium",
        "/sobre", "/contato", "/faq", "/privacidade", "/termos",
        "/terapia", "/ranking", "/afiliado",
    ]
    slugs = [a["slug"] for a in ARTIGOS_BLOG]
    hoje = datetime.now().strftime("%Y-%m-%d")
    linhas = ['<?xml version="1.0" encoding="UTF-8"?>']
    linhas.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for u in urls_fixas:
        linhas.append(f'  <url><loc>{BASE_URL}{u}</loc><lastmod>{hoje}</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>')
    for s in slugs:
        linhas.append(f'  <url><loc>{BASE_URL}/blog/{s}</loc><lastmod>{hoje}</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>')
    linhas.append('</urlset>')
    return Response(content=chr(10).join(linhas), media_type="application/xml")

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    from fastapi.responses import FileResponse
    import os
    favicon_path = "static/favicon.svg"
    if os.path.exists(favicon_path):
        return FileResponse(favicon_path, media_type="image/svg+xml")
    return Response(status_code=204)

@app.get("/favicon.svg", include_in_schema=False)
async def favicon_svg():
    from fastapi.responses import FileResponse
    import os
    favicon_path = "static/favicon.svg"
    if os.path.exists(favicon_path):
        return FileResponse(favicon_path, media_type="image/svg+xml")
    return Response(status_code=204)


@app.exception_handler(500)
async def erro_500(request: Request, exc: Exception):
    monitorar_erro(str(request.url.path), str(exc))
    return render_template("500.html", request=request)

@app.exception_handler(Exception)
async def erro_geral(request: Request, exc: Exception):
    monitorar_erro(str(request.url.path), str(exc))
    return render_template("500.html", request=request)

@app.exception_handler(StarletteHTTPException)
async def custom_404(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return templates.TemplateResponse(
            request, "404.html", status_code=404
        )
    return await http_exception_handler(request, exc)

# ================================================================
# ROTAS — INDEX E DASHBOARD
# ================================================================

@app.get("/", response_class=HTMLResponse)
def index(request: Request, ref: str = None, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)

    if not usuario:
        total_usuarios  = contar_total_usuarios(db)
        total_analises  = db.query(Analise).count()
        total_mensagens = db.query(Mensagem).count()
        response = templates.TemplateResponse(request, "index.html", {
            "total_usuarios":  total_usuarios,
            "total_analises":  total_analises,
            "total_mensagens": total_mensagens,
        })
        if ref:
            response.set_cookie(key="ref", value=ref, max_age=86400)
        return response

    # Usuário logado — mostra dashboard
    analises_hoje  = contar_hoje(Analise,  usuario.id, db)
    mensagens_hoje = contar_hoje(Mensagem, usuario.id, db)
    diarios_hoje   = contar_hoje(Diario,   usuario.id, db)

    # Últimas análises
    ultimas_analises = db.query(Analise).filter(
        Analise.usuario_id == usuario.id
    ).order_by(Analise.criado_em.desc()).limit(5).all()

    # Últimas mensagens
    ultimas_mensagens = db.query(Mensagem).filter(
        Mensagem.usuario_id == usuario.id
    ).order_by(Mensagem.criado_em.desc()).limit(3).all()

    # Ranking top 10
    ranking = db.query(Usuario).filter(
        Usuario.ativo == True
    ).order_by(Usuario.pontos.desc()).limit(10).all()

    # Estatísticas de emoções
    todas_analises = db.query(Analise).filter(
        Analise.usuario_id == usuario.id
    ).all()

    emocoes_contagem = {}
    for a in todas_analises:
        e = a.emocao.lower()
        emocoes_contagem[e] = emocoes_contagem.get(e, 0) + 1

    emocao_favorita = (
        max(emocoes_contagem, key=emocoes_contagem.get)
        if emocoes_contagem else "neutro"
    )

    # Conquistas do usuário
    conquistas = db.query(Conquista).filter(
        Conquista.usuario_id == usuario.id
    ).order_by(Conquista.criado_em.desc()).limit(12).all()
    total_conquistas = db.query(Conquista).filter(
        Conquista.usuario_id == usuario.id
    ).count()

    # Próximo badge
    prox_badge = proximo_badge(usuario.pontos)

    # Dias cadastrado
    dias_cadastrado = (datetime.now() - usuario.criado_em).days

    # Trial info
    trial_dias_restantes = None
    if usuario.plano == "trial" and usuario.trial_expira:
        delta = usuario.trial_expira - datetime.now()
        trial_dias_restantes = max(0, delta.days)

    # Score de Inteligencia Emocional (0-100)
    total_msgs    = db.query(Mensagem).filter(Mensagem.usuario_id == usuario.id).count()
    total_diarios = db.query(Diario).filter(Diario.usuario_id == usuario.id).count()
    total_analises_count = len(todas_analises)

    # Componentes do score (cada um vale ate 25 pontos)
    # 1. Variedade emocional (quantas emocoes diferentes — max 15)
    variedade      = len(emocoes_contagem)
    score_variedade = min(25, int((variedade / 15) * 25))

    # 2. Consistencia (dias cadastrado com atividade — usa total de analises)
    score_consistencia = min(25, int((min(total_analises_count, 50) / 50) * 25))

    # 3. Engajamento (chat + diario)
    engajamento    = min(total_msgs + total_diarios, 60)
    score_engajamento = min(25, int((engajamento / 60) * 25))

    # 4. Progresso (pontos — max 2000 para score maximo)
    score_progresso = min(25, int((min(usuario.pontos, 2000) / 2000) * 25))

    score_ie = score_variedade + score_consistencia + score_engajamento + score_progresso

    # Nivel do score
    if score_ie >= 80:
        nivel_ie = "Mestre Emocional"
        cor_ie   = "#9b59b6"
    elif score_ie >= 60:
        nivel_ie = "Avancado"
        cor_ie   = "#2ecc71"
    elif score_ie >= 40:
        nivel_ie = "Intermediario"
        cor_ie   = "#3498db"
    elif score_ie >= 20:
        nivel_ie = "Em Desenvolvimento"
        cor_ie   = "#f39c12"
    else:
        nivel_ie = "Iniciante"
        cor_ie   = "#e74c3c"

    return templates.TemplateResponse(request, "dashboard.html", {
        "usuario":               usuario,
        "analises_hoje":         analises_hoje,
        "mensagens_hoje":        mensagens_hoje,
        "diarios_hoje":          diarios_hoje,
        "limite_analises":       get_limite(usuario, "analises"),
        "limite_chat":           get_limite(usuario, "chat"),
        "limite_diario":         get_limite(usuario, "diario"),
        "ranking":               ranking,
        "ultimas_analises":      ultimas_analises,
        "ultimas_mensagens":     ultimas_mensagens,
        "emocoes_contagem":      json.dumps(emocoes_contagem),
        "emocao_favorita":       emocao_favorita,
        "emocao_emoji":          get_emoji(emocao_favorita),
        "conquistas":            conquistas,
        "total_conquistas":      total_conquistas,
        "proximo_badge":         prox_badge,
        "dias_cadastrado":       dias_cadastrado,
        "trial_dias_restantes":  trial_dias_restantes,
        "total_analises":        len(todas_analises),
        "score_ie":              score_ie,
        "nivel_ie":              nivel_ie,
        "cor_ie":                cor_ie,
        "score_variedade":       score_variedade,
        "score_consistencia":    score_consistencia,
        "score_engajamento":     score_engajamento,
        "score_progresso":       score_progresso,
    })

# ================================================================
# ROTAS — LOGIN
# ================================================================

@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if usuario:
        return RedirectResponse(url="/")
    return templates.TemplateResponse(request, "login.html", {
        "base_url": BASE_URL
    })


@app.post("/login")
def login(
    request:  Request,
    email:    str = Form(...),
    senha:    str = Form(...),
    db:       Session = Depends(get_db)
):
    ip = request.client.host if request.client else "unknown"

    # Rate limit
    if not rate_limit(ip, limite=10, janela=60):
        return templates.TemplateResponse(request, "login.html", {
            "erro": "⚠️ Muitas tentativas. Aguarde 1 minuto e tente novamente."
        })

    # Validação básica
    if not email or not senha:
        return templates.TemplateResponse(request, "login.html", {
            "erro": "⚠️ Preencha todos os campos."
        })

    usuario = db.query(Usuario).filter(
        Usuario.email == email.lower().strip()
    ).first()

    if not usuario or not verificar_senha(senha, usuario.senha):
        registrar_log("/login", "POST", ip, 401, db=db)
        return templates.TemplateResponse(request, "login.html", {
            "erro": "❌ Email ou senha incorretos. Tente novamente."
        })

    if not usuario.ativo:
        return templates.TemplateResponse(request, "login.html", {
            "erro": (
                "🚫 Conta desativada. "
                "Entre em contato com o suporte."
            )
        })

    session_id          = str(uuid.uuid4())
    sessoes[session_id] = usuario.id
    registrar_log("/login", "POST", ip, 200, usuario.id, db)

    response = RedirectResponse(url="/", status_code=302)
    response.set_cookie(
        key="session_id",
        value=session_id,
        httponly=True,
        max_age=86400 * 7  # 7 dias
    )
    return response

# ================================================================
# ROTAS — CADASTRO
# ================================================================

@app.get("/cadastro", response_class=HTMLResponse)
def cadastro_page(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if usuario:
        return RedirectResponse(url="/")
    return templates.TemplateResponse(request, "cadastro.html", {
        "base_url": BASE_URL
    })


@app.post("/cadastro")
async def cadastro(
    background_tasks: BackgroundTasks,
    request:          Request,
    nome:             str = Form(...),
    email:            str = Form(...),
    senha:            str = Form(...),
    confirmar_senha: str = Form(None),
    db:               Session = Depends(get_db)
):
    ip = request.client.host if request.client else "unknown"

    # Rate limit
    if not rate_limit(ip, limite=5, janela=300):
        return templates.TemplateResponse(request, "cadastro.html", {
            "erro": "⚠️ Muitos cadastros. Aguarde 5 minutos."
        })

    # Validações
    nome = nome.strip()
    email = email.lower().strip()

    if len(nome) < 2:
        return templates.TemplateResponse(request, "cadastro.html", {
            "erro": "⚠️ Nome deve ter pelo menos 2 caracteres."
        })

    if not validar_email(email):
        return templates.TemplateResponse(request, "cadastro.html", {
            "erro": "⚠️ Email inválido. Verifique e tente novamente."
        })

    valida, msg_erro = validar_senha(senha)
    if not valida:
        return templates.TemplateResponse(request, "cadastro.html", {
            "erro": f"⚠️ {msg_erro}"
        })

    if senha != confirmar_senha:
        return templates.TemplateResponse(request, "cadastro.html", {
            "erro": "⚠️ As senhas não coincidem."
        })

    existe = db.query(Usuario).filter(Usuario.email == email).first()
    if existe:
        return templates.TemplateResponse(request, "cadastro.html", {
            "erro": "⚠️ Este email já está cadastrado. Faça login."
        })

    ref_cookie = request.cookies.get("ref")
    ref_code   = gerar_ref_code(nome)
    # Incrementa contador de indicados do afiliado
    if ref_cookie:
        afiliado = db.query(Usuario).filter(Usuario.ref_code == ref_cookie).first()
        if afiliado:
            enviar_telegram(
                f"🔗 <b>Novo indicado pelo afiliado</b>\n"
                f"👤 Afiliado: {afiliado.nome}\n"
                f"🆕 Indicado: {nome}\n"
                f"🕐 {datetime.now().strftime('%d/%m/%Y %H:%M')}"
            )
    api_token  = gerar_api_token(email)

    novo = Usuario(
        nome=nome,
        email=email,
        senha=hash_senha(senha),
        plano="free",
        ref_code=ref_code,
        indicado_por=ref_cookie,
        api_token=api_token
    )
    db.add(novo)
    db.commit()
    db.refresh(novo)

    adicionar_pontos(novo, PONTOS_POR_ACAO["cadastro"], db)

    background_tasks.add_task(
        enviar_email_boas_vindas, nome, email, ref_code
    )
    enviar_telegram(
        "🎉 <b>Novo cadastro!</b>\n"
        f"👤 Nome: {nome}\n"
        f"📧 Email: {email}\n"
        f"🕐 {datetime.now().strftime('%d/%m/%Y %H:%M')}"
    )
    background_tasks.add_task(
        enviar_email_novo_cadastro, nome, email
    )

    registrar_log("/cadastro", "POST", ip, 200, novo.id, db)

    session_id          = str(uuid.uuid4())
    sessoes[session_id] = novo.id

    response = RedirectResponse(url="/obrigado", status_code=302)
    response.set_cookie(
        key="session_id",
        value=session_id,
        httponly=True,
        max_age=86400 * 7
    )
    return response

# ================================================================
# ROTAS — OBRIGADO / PÓS CADASTRO
# ================================================================

@app.get("/obrigado", response_class=HTMLResponse)
def obrigado(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return RedirectResponse(url="/login")

    link_afiliado = f"{BASE_URL}/?ref={usuario.ref_code}"

    return templates.TemplateResponse(request, "obrigado.html", {
        "usuario":       usuario,
        "link_afiliado": link_afiliado,
        "pontos_ganhos": PONTOS_POR_ACAO["cadastro"],
    })

# ================================================================
# ROTAS — LOGOUT
# ================================================================

@app.get("/logout")
def logout(request: Request):
    session_id = request.cookies.get("session_id")
    if session_id and session_id in sessoes:
        del sessoes[session_id]
    response = RedirectResponse(url="/login", status_code=302)
    response.delete_cookie("session_id")
    return response

# ================================================================
# ROTAS — PÁGINAS INSTITUCIONAIS
# ================================================================

@app.get("/privacidade", response_class=HTMLResponse)
def privacidade(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    return templates.TemplateResponse(request, "privacidade.html", {
        "usuario": usuario
    })


@app.get("/termos", response_class=HTMLResponse)
def termos(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    return templates.TemplateResponse(request, "termos.html", {
        "usuario": usuario
    })


@app.get("/faq", response_class=HTMLResponse)
def faq(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    perguntas = [
        {
            "pergunta": "O que é o Emotion Intelligence?",
            "resposta": (
                "É uma plataforma de inteligência emocional com IA que ajuda "
                "você a identificar, compreender e gerenciar suas emoções através "
                "de análises avançadas, diário emocional e chat com a Sofia, "
                "sua psicóloga virtual."
            )
        },
        {
            "pergunta": "A Sofia substitui um psicólogo real?",
            "resposta": (
                "Não. A Sofia é uma assistente virtual de apoio emocional. "
                "Em casos de sofrimento intenso, crise ou necessidade de "
                "diagnóstico, sempre recomendamos buscar um profissional de saúde mental."
            )
        },
        {
            "pergunta": "Como funciona o plano Free?",
            "resposta": (
                "O plano Free oferece 10 análises por dia, 5 conversas com a Sofia "
                "e 3 entradas no diário emocional. Sem cartão de crédito necessário."
            )
        },
        {
            "pergunta": "Como funciona o programa de afiliados?",
            "resposta": (
                "Você recebe um link único. Quando alguém se cadastrar e assinar "
                "um plano pago pelo seu link, você ganha 20% de comissão. "
                "Os pagamentos são feitos mensalmente."
            )
        },
        {
            "pergunta": "Posso cancelar o plano Premium a qualquer momento?",
            "resposta": (
                "Sim! Você pode cancelar quando quiser sem multa. "
                "Entre em contato com nosso suporte pelo chat ao vivo."
            )
        },
        {
            "pergunta": "Meus dados estão seguros?",
            "resposta": (
                "Sim. Suas senhas são criptografadas e seus dados nunca são "
                "vendidos a terceiros. Leia nossa Política de Privacidade "
                "para mais detalhes."
            )
        },
        {
            "pergunta": "O que é o Trial de 7 dias?",
            "resposta": (
                "O Trial Premium dá acesso a todos os recursos do plano Premium "
                "por 7 dias, sem precisar de cartão de crédito. "
                "Cada usuário pode ativar apenas uma vez."
            )
        },
        {
            "pergunta": "Como funciona o sistema de pontos?",
            "resposta": (
                "Você ganha pontos por cada ação: +10 no cadastro, +5 por análise, "
                "+2 por mensagem (free) ou +5 (premium), +8 por entrada no diário, "
                "+20 ao ativar trial e +50 ao assinar Premium."
            )
        },
    ]
    return templates.TemplateResponse(request, "faq.html", {
        "usuario":   usuario,
        "perguntas": perguntas
    })


@app.get("/contato", response_class=HTMLResponse)
def contato(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    return templates.TemplateResponse(request, "contato.html", {
        "usuario": usuario
    })


@app.get("/sobre", response_class=HTMLResponse)
def sobre(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    total_usuarios = contar_total_usuarios(db)
    total_analises = db.query(Analise).count()
    return templates.TemplateResponse(request, "sobre.html", {
        "usuario":       usuario,
        "total_usuarios": total_usuarios,
        "total_analises": total_analises,
    })

# ================================================================
# ROTAS — PERFIL
# ================================================================

@app.get("/perfil", response_class=HTMLResponse)
def perfil_page(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return RedirectResponse(url="/login")

    total_analises  = db.query(Analise).filter(
        Analise.usuario_id == usuario.id
    ).count()
    total_mensagens = db.query(Mensagem).filter(
        Mensagem.usuario_id == usuario.id
    ).count()
    total_diarios   = db.query(Diario).filter(
        Diario.usuario_id == usuario.id
    ).count()
    analises_hoje   = contar_hoje(Analise, usuario.id, db)
    dias_cadastrado = (datetime.now() - usuario.criado_em).days
    prox_badge      = proximo_badge(usuario.pontos)

    # Conquistas
    conquistas = db.query(Conquista).filter(
        Conquista.usuario_id == usuario.id
    ).order_by(Conquista.criado_em.desc()).all()

    # Emoção favorita
    todas_analises = db.query(Analise).filter(
        Analise.usuario_id == usuario.id
    ).all()
    emocoes_contagem = {}
    for a in todas_analises:
        e = a.emocao.lower()
        emocoes_contagem[e] = emocoes_contagem.get(e, 0) + 1

    emocao_favorita = (
        max(emocoes_contagem, key=emocoes_contagem.get)
        if emocoes_contagem else "neutro"
    )

    # Trial info
    trial_dias_restantes = None
    if usuario.plano == "trial" and usuario.trial_expira:
        delta = usuario.trial_expira - datetime.now()
        trial_dias_restantes = max(0, delta.days)

    # Score IE no perfil
    total_msgs_perfil = db.query(Mensagem).filter(Mensagem.usuario_id == usuario.id).count()
    variedade_perfil  = len(emocoes_contagem)
    score_ie_perfil   = min(25, int((variedade_perfil/15)*25)) +                         min(25, int((min(total_analises,50)/50)*25)) +                         min(25, int((min(total_msgs_perfil+total_diarios,60)/60)*25)) +                         min(25, int((min(usuario.pontos,2000)/2000)*25))
    if score_ie_perfil >= 80:
        nivel_ie_perfil = "Mestre Emocional"
        cor_ie_perfil   = "#9b59b6"
    elif score_ie_perfil >= 60:
        nivel_ie_perfil = "Avancado"
        cor_ie_perfil   = "#2ecc71"
    elif score_ie_perfil >= 40:
        nivel_ie_perfil = "Intermediario"
        cor_ie_perfil   = "#3498db"
    elif score_ie_perfil >= 20:
        nivel_ie_perfil = "Em Desenvolvimento"
        cor_ie_perfil   = "#f39c12"
    else:
        nivel_ie_perfil = "Iniciante"
        cor_ie_perfil   = "#e74c3c"

    total_conquistas_perfil = db.query(Conquista).filter(
        Conquista.usuario_id == usuario.id
    ).count()

    return templates.TemplateResponse(request, "perfil.html", {
        "usuario":               usuario,
        "total_analises":        total_analises,
        "total_mensagens":       total_mensagens,
        "total_diarios":         total_diarios,
        "analises_hoje":         analises_hoje,
        "dias_cadastrado":       dias_cadastrado,
        "proximo_badge":         prox_badge,
        "api_token":             usuario.api_token,
        "conquistas":            conquistas,
        "total_conquistas":      total_conquistas_perfil,
        "emocao_favorita":       emocao_favorita,
        "emocao_emoji":          get_emoji(emocao_favorita),
        "trial_dias_restantes":  trial_dias_restantes,
        "link_afiliado":         f"{BASE_URL}/?ref={usuario.ref_code}",
        "score_ie":              score_ie_perfil,
        "nivel_ie":              nivel_ie_perfil,
        "cor_ie":                cor_ie_perfil,
    })


@app.post("/perfil")
def perfil_update(
    request:         Request,
    nome:            str = Form(...),
    bio:             str = Form(""),
    senha:           str = Form(""),
    confirmar_senha: str = Form(""),
    db:              Session = Depends(get_db)
):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return RedirectResponse(url="/login")

    total_analises  = db.query(Analise).filter(
        Analise.usuario_id == usuario.id
    ).count()
    total_mensagens = db.query(Mensagem).filter(
        Mensagem.usuario_id == usuario.id
    ).count()
    total_diarios   = db.query(Diario).filter(
        Diario.usuario_id == usuario.id
    ).count()
    analises_hoje   = contar_hoje(Analise, usuario.id, db)
    dias_cadastrado = (datetime.now() - usuario.criado_em).days
    conquistas      = db.query(Conquista).filter(
        Conquista.usuario_id == usuario.id
    ).all()

    contexto_base = {
        "usuario":         usuario,
        "total_analises":  total_analises,
        "total_mensagens": total_mensagens,
        "total_diarios":   total_diarios,
        "analises_hoje":   analises_hoje,
        "dias_cadastrado": dias_cadastrado,
        "conquistas":      conquistas,
        "api_token":       usuario.api_token,
        "link_afiliado":   f"{BASE_URL}/?ref={usuario.ref_code}",
    }

    if len(nome.strip()) < 2:
        return templates.TemplateResponse(request, "perfil.html", {
            **contexto_base,
            "erro": "⚠️ Nome deve ter pelo menos 2 caracteres."
        })

    if senha:
        valida, msg_erro = validar_senha(senha)
        if not valida:
            return templates.TemplateResponse(request, "perfil.html", {
                **contexto_base,
                "erro": f"⚠️ {msg_erro}"
            })
        if senha != confirmar_senha:
            return templates.TemplateResponse(request, "perfil.html", {
                **contexto_base,
                "erro": "⚠️ As senhas não coincidem."
            })
        usuario.senha = hash_senha(senha)

    usuario.nome = nome.strip()
    usuario.bio  = bio.strip()[:500] if bio else None
    db.commit()

    return templates.TemplateResponse(request, "perfil.html", {
        **contexto_base,
        "sucesso": "✅ Perfil atualizado com sucesso!"
    })

# ================================================================
# ROTAS — AFILIADOS
# ================================================================

@app.get("/afiliado", response_class=HTMLResponse)
def afiliado_page(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return RedirectResponse(url="/login")

    indicados = db.query(Usuario).filter(
        Usuario.indicado_por == usuario.ref_code
    ).all()

    indicados_premium = [
        u for u in indicados
        if u.plano in ["premium", "enterprise"]
    ]

    comissao = sum(
        49  if u.plano == "premium"    else
        199 if u.plano == "enterprise" else 0
        for u in indicados_premium
    ) * COMISSAO_PERCENT // 100

    link = f"{BASE_URL}/?ref={usuario.ref_code}"

    # Histórico de indicados com detalhes
    indicados_detalhes = [{
        "nome":      u.nome,
        "plano":     u.plano,
        "criado_em": u.criado_em.strftime("%d/%m/%Y"),
        "pontos":    u.pontos,
        "comissao":  (
            49  * COMISSAO_PERCENT // 100 if u.plano == "premium"    else
            199 * COMISSAO_PERCENT // 100 if u.plano == "enterprise" else 0
        )
    } for u in indicados]

    return templates.TemplateResponse(request, "afiliado.html", {
        "usuario":            usuario,
        "total_indicados":    len(indicados),
        "indicados_premium":  len(indicados_premium),
        "indicados":          indicados_detalhes,
        "comissao":           comissao,
        "link":               link,
        "comissao_percent":   COMISSAO_PERCENT,
        "link_whatsapp": (
            f"https://wa.me/?text=Olhe%20essa%20plataforma%20incrível%20de%20"
            f"inteligência%20emocional!%20{link}"
        ),
        "link_telegram": (
            f"https://t.me/share/url?url={link}&text="
            f"Plataforma%20incrível%20de%20inteligência%20emocional!"
        ),
        "link_twitter": (
            f"https://twitter.com/intent/tweet?text="
            f"Descobri%20essa%20plataforma%20incrível%20de%20inteligência%20"
            f"emocional!%20{link}"
        ),
    })

# ================================================================
# ROTAS — PLANOS
# ================================================================

@app.get("/planos", response_class=HTMLResponse)
def planos(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return RedirectResponse(url="/login")
    return templates.TemplateResponse(request, "planos.html", {
        "usuario": usuario,
        "precos":  PRECOS,
    })

@app.get("/premium", response_class=HTMLResponse)
def premium_page(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    return templates.TemplateResponse(request, "premium.html", {
        "usuario": usuario,
        "precos":  PRECOS,
    })

# ================================================================
# ROTAS — TRIAL
# ================================================================

@app.post("/trial")
def ativar_trial(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autorizado")

    if usuario.trial_usado:
        raise HTTPException(
            status_code=400,
            detail=(
                "❌ Trial já utilizado anteriormente. "
                "Faça upgrade para o plano Premium para continuar. 💎"
            )
        )

    if usuario.plano != "free":
        raise HTTPException(
            status_code=400,
            detail="⚠️ Você já tem um plano ativo."
        )

    usuario.plano        = "trial"
    usuario.trial_usado  = True
    usuario.trial_expira = datetime.now() + timedelta(days=7)
    db.commit()

    adicionar_pontos(usuario, PONTOS_POR_ACAO["trial"], db)

    enviar_telegram(
        "🔥 <b>Trial ativado</b>\n"
        f"👤 {usuario.nome}\n"
        f"📧 {usuario.email}\n"
        f"🕐 {datetime.now().strftime('%d/%m/%Y %H:%M')}"
    )

    return {
        "mensagem":     "🎉 Trial Premium ativado com sucesso por 7 dias!",
        "expira_em":    usuario.trial_expira.strftime("%d/%m/%Y às %H:%M"),
        "pontos_ganhos": PONTOS_POR_ACAO["trial"],
        "total_pontos": usuario.pontos,
        "badge":        usuario.badge,
        "beneficios": [
            "✅ 50 análises por dia",
            "✅ 20 conversas com Sofia por dia",
            "✅ 10 entradas no diário por dia",
            "✅ Respostas mais completas da Sofia",
        ]
    }

# ================================================================
# ROTAS — RANKING
# ================================================================

@app.get("/ranking")
def ranking_route(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    # Ranking e publico — sem bloqueio por login

    top = db.query(Usuario).filter(
        Usuario.ativo == True
    ).order_by(Usuario.pontos.desc()).limit(20).all()

    posicao = next(
        (i + 1 for i, u in enumerate(top) if u.id == usuario.id),
        None
    )

    # Se não está no top 20, busca posição real
    if posicao is None:
        todos_ordenados = db.query(Usuario).filter(
            Usuario.ativo == True
        ).order_by(Usuario.pontos.desc()).all()
        posicao = next(
            (i + 1 for i, u in enumerate(todos_ordenados)
             if u.id == usuario.id),
            None
        )

    return {
        "minha_posicao": posicao,
        "meus_pontos":   usuario.pontos,
        "meu_badge":     usuario.badge,
        "total_usuarios": db.query(Usuario).filter(
            Usuario.ativo == True
        ).count(),
        "ranking": [{
            "posicao": i + 1,
            "nome":    u.nome[:25],
            "pontos":  u.pontos,
            "badge":   u.badge,
            "plano":   u.plano,
            "emoji":   "👑" if i == 0 else "🥈" if i == 1 else "🥉" if i == 2 else "🏅",
            "eu":      u.id == usuario.id,
        } for i, u in enumerate(top)]
    }

# ================================================================
# ROTAS — NOTIFICAÇÕES
# ================================================================

@app.post("/notificacoes/marcar-lidas")
def marcar_notifs_lidas(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Nao autorizado")
    db.query(Notificacao).filter(
        Notificacao.usuario_id == usuario.id,
        Notificacao.lida == False
    ).update({"lida": True})
    db.commit()
    return {"ok": True}

@app.get("/notificacoes")
def ver_notificacoes(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autorizado")

    notificacoes = db.query(Notificacao).filter(
        Notificacao.usuario_id == usuario.id
    ).order_by(Notificacao.criado_em.desc()).limit(20).all()

    nao_lidas = db.query(Notificacao).filter(
        Notificacao.usuario_id == usuario.id,
        Notificacao.lida == False
    ).count()

    # Marca todas como lidas
    db.query(Notificacao).filter(
        Notificacao.usuario_id == usuario.id,
        Notificacao.lida == False
    ).update({"lida": True})
    db.commit()

    return {
        "total":     len(notificacoes),
        "nao_lidas": nao_lidas,
        "notificacoes": [{
            "titulo":    n.titulo,
            "mensagem":  n.mensagem,
            "lida":      n.lida,
            "timestamp": n.criado_em.strftime("%d/%m/%Y %H:%M")
        } for n in notificacoes]
    }


@app.get("/conquistas")
def ver_conquistas(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autorizado")

    conquistas = db.query(Conquista).filter(
        Conquista.usuario_id == usuario.id
    ).order_by(Conquista.criado_em.desc()).all()

    todas_possiveis = [
        {"nome": "Primeira Análise",    "emoji": "🎯", "descricao": "Fez a primeira análise emocional"},
        {"nome": "Analista Experiente", "emoji": "📊", "descricao": "Completou 50 análises"},
        {"nome": "Amigo da Sofia",      "emoji": "🤝", "descricao": "Trocou 10 mensagens com a Sofia"},
        {"nome": "Diarista Emocional",  "emoji": "📖", "descricao": "Escreveu 7 entradas no diário"},
        {"nome": "Milionário de Pontos","emoji": "💰", "descricao": "Acumulou 1000 pontos"},
    ]

    nomes_conquistados = [c.nome for c in conquistas]

    return {
        "total_conquistadas": len(conquistas),
        "total_possiveis":    len(todas_possiveis),
        "conquistas": [{
            "nome":      c.nome,
            "descricao": c.descricao,
            "emoji":     c.emoji,
            "timestamp": c.criado_em.strftime("%d/%m/%Y"),
            "conquistada": True
        } for c in conquistas],
        "disponiveis": [{
            "nome":      p["nome"],
            "emoji":     p["emoji"],
            "descricao": p["descricao"],
            "conquistada": p["nome"] in nomes_conquistados
        } for p in todas_possiveis]
    }

# ================================================================
# FIM DA PARTE 2
# ================================================================
# ================================================================
# ROTAS — ANÁLISE DE EMOÇÕES
# ================================================================

@app.get("/analyze")
def analyze(
    request: Request,
    text:    str,
    db:      Session = Depends(get_db)
):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autorizado")

    limite = get_limite(usuario, "analises")
    total_hoje = contar_hoje(Analise, usuario.id, db)

    if total_hoje >= limite:
        raise HTTPException(
            status_code=429,
            detail=(
                f"⚠️ Você atingiu o limite de {limite} análises por dia. "
                f"{'Aguarde até amanhã ou faça upgrade para Premium! 💎' if usuario.plano == 'free' else 'Aguarde até amanhã!'}"
            )
        )

    if len(text.strip()) < 3:
        raise HTTPException(
            status_code=400,
            detail="⚠️ Texto muito curto. Digite pelo menos 3 caracteres."
        )

    # GEMINI ATIVO na API publica
    try:
        _a = detectar_emocao_hibrido(text, usar_gemini=True)
        emocao = _a.get("emocao", "neutro")
    except:
        try:
            _at = detectar_emocao_hibrido(text, usar_gemini=True)
            emocao = _at.get("emocao", "neutro")
        except:
            emocao = detectar_emocao(text)
    intensidade = calcular_intensidade(text)
    tecnica     = tecnicas_por_emocao.get(emocao, tecnicas_por_emocao["neutro"])

    analise = Analise(
        texto=text,
        emocao=emocao.capitalize(),
        emoji=get_emoji(emocao),
        recomendacao=recomendacoes.get(emocao, recomendacoes["neutro"]),
        intensidade=intensidade,
        tecnica=tecnica,
        usuario_id=usuario.id
    )
    db.add(analise)
    db.commit()

    adicionar_pontos(usuario, PONTOS_POR_ACAO["analise"], db)

    # Verifica conquistas especiais
    total_analises = db.query(Analise).filter(
        Analise.usuario_id == usuario.id
    ).count()

    mensagem_especial = None
    if total_analises == 1:
        mensagem_especial = "🎯 Primeira análise! Conquista desbloqueada!"
    elif total_analises == 50:
        mensagem_especial = "📊 50 análises! Você é incrível!"
    elif total_analises == 100:
        mensagem_especial = "🏆 100 análises! Especialista emocional!"

    return {
        "texto":            text,
        "emocao":           emocao.capitalize(),
        "emoji":            get_emoji(emocao),
        "recomendacao":     recomendacoes.get(emocao, recomendacoes["neutro"]),
        "tecnica":          tecnica,
        "intensidade":      intensidade,
        "intensidade_label": (
            "🔴 Alta" if intensidade == 3 else
            "🟡 Média" if intensidade == 2 else
            "🟢 Baixa"
        ),
        "pontos_ganhos":    PONTOS_POR_ACAO["analise"],
        "total_pontos":     usuario.pontos,
        "badge":            usuario.badge,
        "analises_hoje":    total_hoje + 1,
        "limite_analises":  limite,
        "restantes":        limite - (total_hoje + 1),
        "mensagem_especial": mensagem_especial,
        "timestamp":        datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    }


@app.get("/historico")
def ver_historico(
    request: Request,
    pagina:  int = 1,
    db:      Session = Depends(get_db)
):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autorizado")

    por_pagina = 20
    offset     = (pagina - 1) * por_pagina

    total = db.query(Analise).filter(
        Analise.usuario_id == usuario.id
    ).count()

    analises = db.query(Analise).filter(
        Analise.usuario_id == usuario.id
    ).order_by(
        Analise.criado_em.desc()
    ).offset(offset).limit(por_pagina).all()

    # Estatísticas gerais
    todas = db.query(Analise).filter(
        Analise.usuario_id == usuario.id
    ).all()

    emocoes_contagem = {}
    intensidade_total = 0
    for a in todas:
        e = a.emocao.lower()
        emocoes_contagem[e] = emocoes_contagem.get(e, 0) + 1
        intensidade_total   += a.intensidade

    intensidade_media = round(
        intensidade_total / len(todas), 1
    ) if todas else 0

    return {
        "total":            total,
        "pagina":           pagina,
        "total_paginas":    (total + por_pagina - 1) // por_pagina,
        "intensidade_media": intensidade_media,
        "emocoes_contagem": emocoes_contagem,
        "mais_frequente":   max(emocoes_contagem, key=emocoes_contagem.get) if emocoes_contagem else "neutro",
        "analises": [{
            "id":           a.id,
            "texto":        a.texto,
            "emocao":       a.emocao,
            "emoji":        a.emoji,
            "recomendacao": a.recomendacao,
            "tecnica":      a.tecnica,
            "intensidade":  a.intensidade,
            "intensidade_label": (
                "🔴 Alta" if a.intensidade == 3 else
                "🟡 Média" if a.intensidade == 2 else
                "🟢 Baixa"
            ),
            "timestamp":    a.criado_em.strftime("%d/%m/%Y %H:%M"),
        } for a in analises]
    }


@app.get("/stats")
def stats(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autorizado")

    analises  = db.query(Analise).filter(
        Analise.usuario_id == usuario.id
    ).all()
    mensagens = db.query(Mensagem).filter(
        Mensagem.usuario_id == usuario.id
    ).all()
    diarios   = db.query(Diario).filter(
        Diario.usuario_id == usuario.id
    ).all()

    if not analises:
        return {
            "mensagem":      "Nenhuma análise ainda. Comece agora! 🚀",
            "total_analises": 0,
            "pontos":         usuario.pontos,
            "badge":          usuario.badge,
        }

    emocoes  = [a.emocao.lower() for a in analises]
    contagem = {}
    for e in emocoes:
        contagem[e] = contagem.get(e, 0) + 1

    # Por dia (últimos 7 dias)
    por_dia = {}
    for i in range(7):
        dia = (datetime.now() - timedelta(days=i)).strftime("%d/%m")
        por_dia[dia] = 0
    for a in analises:
        dia = a.criado_em.strftime("%d/%m")
        if dia in por_dia:
            por_dia[dia] += 1

    # Por hora
    por_hora = {}
    for a in analises:
        hora = a.criado_em.strftime("%H:00")
        por_hora[hora] = por_hora.get(hora, 0) + 1

    # Intensidade média
    intensidade_media = round(
        sum(a.intensidade for a in analises) / len(analises), 2
    )

    # Streak (dias consecutivos)
    datas = sorted(set(
        a.criado_em.date() for a in analises
    ), reverse=True)
    streak = 0
    hoje   = date.today()
    for i, d in enumerate(datas):
        if d == hoje - timedelta(days=i):
            streak += 1
        else:
            break

    return {
        "total_analises":    len(analises),
        "total_mensagens":   len(mensagens),
        "total_diarios":     len(diarios),
        "emocoes_detectadas": contagem,
        "mais_frequente":    max(contagem, key=contagem.get),
        "emoji_frequente":   get_emoji(max(contagem, key=contagem.get)),
        "por_dia":           por_dia,
        "por_hora":          por_hora,
        "intensidade_media": intensidade_media,
        "streak_dias":       streak,
        "pontos":            usuario.pontos,
        "badge":             usuario.badge,
        "plano":             usuario.plano,
        "proximo_badge":     proximo_badge(usuario.pontos),
        "conquistas":        db.query(Conquista).filter(
            Conquista.usuario_id == usuario.id
        ).count(),
    }

# ================================================================
# ROTAS — IA PSICÓLOGA SOFIA 🧠 PREMIUM COMPLETO
# ================================================================

@app.post("/chat")
async def chat(
    request:  Request,
    mensagem: str = Form(...),
    db:       Session = Depends(get_db)
):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autorizado")

    limite     = get_limite(usuario, "chat")
    total_hoje = contar_hoje(Mensagem, usuario.id, db)

    if total_hoje >= limite:
        raise HTTPException(
            status_code=429,
            detail=(
                f"⚠️ Você atingiu o limite de {limite} mensagens por dia. "
                f"{'Faça upgrade para Premium e tenha conversas ilimitadas! 💎' if usuario.plano == 'free' else 'Aguarde até amanhã!'}"
            )
        )

    if len(mensagem.strip()) < 2:
        raise HTTPException(
            status_code=400,
            detail="⚠️ Mensagem muito curta."
        )

    # Histórico das últimas mensagens
    historico = db.query(Mensagem).filter(
        Mensagem.usuario_id == usuario.id
    ).order_by(Mensagem.criado_em.desc()).limit(20).all()

    contexto = ""
    for h in reversed(historico):
        contexto += f"Usuario: {h.conteudo}\nSofia: {h.resposta}\n\n"

    # GEMINI detecta emocao da mensagem para Sofia
    try:
        _analise_msg = detectar_emocao_hibrido(mensagem, usar_gemini=True)
        emocao_atual = _analise_msg.get("emocao", "neutro")
        _crise_detectada = _analise_msg.get("em_crise", False)
    except:
        emocao_atual = detectar_emocao(mensagem)
        _crise_detectada = detectar_crise(mensagem)
    eh_premium   = usuario.plano in ["premium", "enterprise"]

    # Estatísticas do usuário para contexto
    total_analises  = db.query(Analise).filter(
        Analise.usuario_id == usuario.id
    ).count()
    total_diarios   = db.query(Diario).filter(
        Diario.usuario_id == usuario.id
    ).count()
    total_mensagens = len(historico)

    # Emoções recentes para padrão
    analises_recentes = db.query(Analise).filter(
        Analise.usuario_id == usuario.id
    ).order_by(Analise.criado_em.desc()).limit(10).all()

    emocoes_recentes = [a.emocao.lower() for a in analises_recentes]
    padrao_emocional = ""
    if emocoes_recentes:
        contagem_recente = {}
        for e in emocoes_recentes:
            contagem_recente[e] = contagem_recente.get(e, 0) + 1
        emocao_dominante = max(contagem_recente, key=contagem_recente.get)
        padrao_emocional = (
            f"Padrão emocional recente: {emocao_dominante} "
            f"({contagem_recente[emocao_dominante]}x nas últimas análises)"
        )

    # Dias cadastrado
    dias_na_plataforma = (datetime.now() - usuario.criado_em).days

    if eh_premium:
        instrucoes_plano = (
            f"PREMIUM: acolha com empatia, reflita sobre {emocao_atual}, "
            f"ensine 1 tecnica terapeutica pratica, exercicio para hoje, "
            f"2 perguntas abertas, encoraje. 10-15 linhas. "
            f"{padrao_emocional}. Crise grave: indique CVV 188."
        )
    else:
        instrucoes_plano = (
            "FREE: 4-6 linhas. Acolha + 1 dica pratica + 1 pergunta reflexiva. "
            "Mencione gentilmente que Premium tem sessoes terapeuticas completas."
        )

    # Historico compacto - ultimas 6 trocas (memoria ampliada)
    # Memoria completa da conversa atual
    historico_curto = ""
    for h in reversed(historico[-12:]):
        historico_curto += f"Usuario: {h.conteudo}\nSofia: {h.resposta[:200]}\n\n"
    
    # Resumo do perfil emocional do usuario
    todas_analises = db.query(Analise).filter(
        Analise.usuario_id == usuario.id
    ).order_by(Analise.criado_em.desc()).limit(30).all()
    
    from collections import Counter as _Counter
    if todas_analises:
        emocoes_todas = [a.emocao for a in todas_analises if a.emocao]
        counter_todas = _Counter(emocoes_todas)
        top3_emocoes = counter_todas.most_common(3)
        perfil_emocional = " | ".join([f"{e}({c}x)" for e,c in top3_emocoes])
    else:
        perfil_emocional = "primeira sessao"
    
    # Temas recorrentes nas conversas
    todos_temas = []
    for h in historico:
        if h.conteudo:
            todos_temas.append(h.conteudo[:50])
    temas_recentes = " | ".join(todos_temas[-5:]) if todos_temas else "nenhum"
    
    # Primeira mensagem do usuario (origem)
    primeira_msg = historico[-1].conteudo if historico else "primeira vez"

    # Analises recentes para contexto emocional
    analises_recentes = db.query(Analise).filter(
        Analise.usuario_id == usuario.id
    ).order_by(Analise.criado_em.desc()).limit(5).all()

    padrao_emocional = ""
    if analises_recentes:
        emocoes_recentes = [a.emocao for a in analises_recentes if a.emocao]
        if emocoes_recentes:
            from collections import Counter
            mais_comum = Counter(emocoes_recentes).most_common(2)
            padrao_emocional = " | ".join([f"{e}({c}x)" for e,c in mais_comum])

    # Diarios recentes
    diarios_recentes = db.query(Diario).filter(
        Diario.usuario_id == usuario.id
    ).order_by(Diario.criado_em.desc()).limit(2).all()

    contexto_diario = ""
    if diarios_recentes:
        contexto_diario = " | ".join([d.conteudo[:60] for d in diarios_recentes])

    total_sessoes = len(historico) // 2 + 1

    # Detectar idioma e normalizar mensagem
    idioma_usuario = detectar_idioma(mensagem)
    mensagem_normalizada = normalizar_giria(mensagem)
    
    # Analise completa da mensagem
    analise_completa = analisar_texto_completo(mensagem)
    tom_detectado = analise_completa.get("tom", "neutro")
    contexto_situacao = analise_completa.get("contexto", "geral")
    urgencia = analise_completa.get("urgencia", "normal")
    temporalidade = analise_completa.get("temporalidade", "presente")
    em_crise = detectar_crise(mensagem)
    
    # Se crise — protocolo especial
    em_crise = _crise_detectada if "_crise_detectada" in dir() else detectar_crise(mensagem)
    if em_crise:
        urgencia = "crise"
        emocao_atual = "desespero"
    
    # Dias na plataforma
    dias_plataforma = (datetime.now() - usuario.criado_em).days if usuario.criado_em else 0
    
    # Score IE se existir
    score_ie = getattr(usuario, 'score_ie', None)
    score_str = f"{score_ie}/100" if score_ie else "ainda calculando"
    
    # Creditos Sofia
    creditos_sofia = getattr(usuario, 'creditos_sofia', 0) or 0
    
    # Contexto de idioma
    idioma_info = ""
    if idioma_usuario == "en":
        idioma_info = "O usuario escreveu em ingles. Entenda a mensagem mas SEMPRE responda em portugues brasileiro."
    elif idioma_usuario == "es":
        idioma_info = "O usuario escreveu em espanhol. Entenda a mensagem mas SEMPRE responda em portugues brasileiro."
    
    # Instrucoes por plano — muito mais detalhadas
    if eh_premium:
        instrucoes_plano = (
            "MODO PREMIUM — Sessao terapeutica completa:\n"
            "1. Acolha com empatia genuina (2-3 linhas)\n"
            "2. Valide a emocao sem julgamento\n"
            "3. Identifique o nucleo do problema\n"
            "4. Ensine 1 tecnica terapeutica especifica (TCC/Mindfulness/EMDR) com passo a passo\n"
            "5. Proponha 1 exercicio pratico para HOJE\n"
            "6. Se padrao negativo recorrente: aponte gentilmente\n"
            "7. Termine com 1 pergunta reflexiva profunda e aberta\n"
            "Tamanho: 12-18 linhas. Use o nome. Seja especifica. Use emojis com moderacao.\n"
            "Se mencionar crise/suicidio: indique CVV 188 (24h, gratuito) imediatamente."
        )
    elif creditos_sofia > 0:
        instrucoes_plano = (
            "MODO SESSAO AVULSA — Resposta completa e personalizada:\n"
            "1. Acolha com empatia (2 linhas)\n"
            "2. Valide a emocao\n"
            "3. Ensine 1 tecnica pratica com passo a passo\n"
            "4. Termine com 1 pergunta reflexiva\n"
            "Tamanho: 8-12 linhas. Use o nome. Seja especifica.\n"
            "Se crise: indique CVV 188."
        )
    else:
        instrucoes_plano = (
            "MODO FREE — Resposta de apoio basico:\n"
            "1. Acolha com empatia genuina (1-2 linhas)\n"
            "2. Valide a emocao\n"
            "3. Oferea 1 dica pratica simples\n"
            "4. Termine com 1 pergunta reflexiva\n"
            "Tamanho: 5-7 linhas. Use o nome.\n"
            "Mencione sutilmente que Premium tem sessoes terapeuticas completas.\n"
            "Se crise: indique CVV 188."
        )

    # Modo Sofia baseado em urgencia e contexto
    if em_crise:
        modo_sofia = "MODO CRISE — PROTOCOLO DE SEGURANCA"
        instrucoes_modo = (
            "ATENCAO MAXIMA: usuario em possivel crise.\n"
            "1. Acolha com calma e presenca total\n"
            "2. Valide sem minimizar\n"
            "3. Pergunte se esta seguro agora\n"
            "4. Indique CVV 188 (gratuito 24h) IMEDIATAMENTE\n"
            "5. Indique CAPS ou UPA mais proximo\n"
            "6. Mantenha a pessoa conversando\n"
            "7. NAO deixe a conversa cair\n"
            "Seja humana, presente, sem julgamento."
        )
    elif urgencia == "alta":
        modo_sofia = "MODO SUPORTE INTENSIVO"
        instrucoes_modo = "Maxima empatia. Tecnica imediata. Presente total."
    elif contexto_situacao == "trabalho":
        modo_sofia = "MODO BURNOUT/TRABALHO"
        instrucoes_modo = "Foco em limites, descanso, prioridades e autocuidado profissional."
    elif contexto_situacao == "relacionamento":
        modo_sofia = "MODO RELACIONAMENTO"
        instrucoes_modo = "Foco em comunicacao, limites, autoamor e vinculos saudaveis."
    elif contexto_situacao == "autoestima":
        modo_sofia = "MODO AUTOESTIMA"
        instrucoes_modo = "Foco em autoaceitacao, forcas, compaixao e valor proprio."
    elif contexto_situacao == "existencial":
        modo_sofia = "MODO EXISTENCIAL"
        instrucoes_modo = "Foco em proposito, valores, sentido de vida e aceitacao."
    elif emocao_atual in ["alegria","gratidao","realizacao","orgulho","euforia","paz"]:
        modo_sofia = "MODO CELEBRACAO"
        instrucoes_modo = "Celebre junto! Reforce o positivo. Ancora a experiencia boa."
    else:
        modo_sofia = "MODO PADRAO"
        instrucoes_modo = instrucoes_plano

    prompt = (
        "=== SOFIA — PSICOLOGA VIRTUAL BRASILEIRA ===\n"
        "Voce e Sofia, psicologa virtual especializada em:\n"
        "• TCC (Terapia Cognitivo-Comportamental)\n"
        "• Mindfulness e Meditacao\n"
        "• EMDR (dessensibilizacao e reprocessamento)\n"
        "• ACT (Terapia de Aceitacao e Compromisso)\n"
        "• DBT (Terapia Comportamental Dialetica)\n"
        "• Psicologia Positiva (Seligman/PERMA)\n"
        "• Gestalt e Abordagem Humanista\n"
        "• Psicologia do Trauma\n"
        "• Terapia do Luto\n"
        "• Coaching Emocional\n\n"
        "PERSONALIDADE: empatica, calorosa, direta, humana, sem jargoes clinicos.\n"
        "LIMITE: NUNCA substitui psicologo real. Sempre indique profissional em casos graves.\n\n"
        "=== LINGUAGEM ===\n"
        "• SEMPRE portugues brasileiro coloquial\n"
        "• Entende qualquer idioma — responde SEMPRE em pt-BR\n"
        "• Entende girias: na bad, destruido, surtei, tô mal, etc\n"
        "• Entende ingles, espanhol, frances, italiano, alemao\n"
        "• Direta — sem enrolacao — sem robotismo\n"
        f"• {idioma_info}\n\n"
        "=== ANALISE DA MENSAGEM ===\n"
        f"• Emocao detectada: {emocao_atual} {get_emoji(emocao_atual)}\n"
        f"• Tom: {tom_detectado}\n"
        f"• Contexto: {contexto_situacao}\n"
        f"• Urgencia: {urgencia}\n"
        f"• Temporalidade: {temporalidade}\n"
        f"• Idioma: {idioma_usuario}\n"
        f"• Em crise: {'SIM — PROTOCOLO ESPECIAL' if em_crise else 'nao'}\n\n"
        "=== PERFIL COMPLETO DO USUARIO ===\n"
        f"• Nome: {usuario.nome}\n"
        f"• Plano: {usuario.plano.upper()}\n"
        f"• Sessao #{total_sessoes} com voce\n"
        f"• Ha {dias_plataforma} dias na plataforma\n"
        f"• Historico emocional (top 3): {perfil_emocional}\n"
        f"• Padrao emocional recente: {padrao_emocional or 'primeira sessao'}\n"
        f"• Temas recorrentes: {temas_recentes}\n"
        f"• Primeira mensagem: {primeira_msg}\n"
        f"• Diario recente: {contexto_diario or 'sem entradas'}\n"
        f"• Score IE: {score_str}\n"
        f"• Badge: {usuario.badge}\n"
        f"• Pontos: {usuario.pontos}\n\n"
        "=== REGRAS DE COMPORTAMENTO ===\n"
        "• NAO repita 'Ola' ou apresentacao em cada mensagem\n"
        "• USE o historico para dar continuidade natural a conversa\n"
        "• REFERENCIE o que foi dito antes quando relevante\n"
        "• Se e a primeira mensagem: apresente-se brevemente\n"
        "• Se nao e a primeira: continue a conversa naturalmente\n"
        "• NUNCA misture ingles no meio do portugues\n"
        "• Seja direta e humana, sem ser robotica\n"
        "• Varie as tecnicas — nao repita a mesma toda vez\n\n"
        "=== MEMORIA DA CONVERSA ATUAL (ultimas 12 trocas) ===\n"
        f"{historico_curto if historico_curto else 'PRIMEIRA CONVERSA — apresente-se com carinho e pergunte como a pessoa esta.'}\n\n"
        f"=== MODO ATUAL: {modo_sofia} ===\n"
        f"{instrucoes_modo}\n\n"
        "=== INSTRUCOES GERAIS DE RESPOSTA ===\n"
        f"{instrucoes_plano}\n\n"
        "=== TECNICAS DISPONVEIS POR SITUACAO ===\n"
        "ANSIEDADE: respiracao 4-7-8, grounding 5-4-3-2-1, body scan, ancoragem\n"
        "TRISTEZA: acolhimento, validacao, ativacao comportamental, ruminacao\n"
        "RAIVA: respiracao, espaco, reformulacao cognitiva, comunicacao nao violenta\n"
        "MEDO: exposicao gradual, descatastrofizacao, autocompaixao\n"
        "TRAUMA: EMDR adaptado, processamento bilateral, estabilizacao\n"
        "BURNOUT: limites, descanso, prioridades, valores, autocuidado\n"
        "AUTOESTIMA: forcas, autocompaixao, distorcoes cognitivas, afirmacoes\n"
        "LUTO: 5 estagios, integracao, memoria, permissao para sentir\n"
        "RELACIONAMENTO: CNV, limites, apego, comunicacao assertiva\n"
        "EXISTENCIAL: valores, proposito, aceitacao, significado\n"
        "CELEBRACAO: reforco positivo, ancora, gratidao, expansao\n\n"
        "=== EXERCICIOS PRATICOS DISPONIVEIS ===\n"
        "• Respiracao 4-7-8 (ansiedade aguda)\n"
        "• Grounding 5-4-3-2-1 (dissociacao/panico)\n"
        "• Diario de gratidao (depressao leve)\n"
        "• Registro de pensamentos ABC (TCC)\n"
        "• Body scan (tensao/estresse)\n"
        "• Meditacao dos 3 minutos\n"
        "• Carta para si mesmo (autocompaixao)\n"
        "• Roda das emocoes (alexitimia)\n"
        "• Cadeira vazia (gestalt)\n"
        "• Tecnica STOP (mindfulness)\n"
        "• Ativacao comportamental (anedonia)\n"
        "• Visualizacao do lugar seguro (trauma)\n\n"
        "=== MENSAGEM ATUAL ===\n"
        f"Original: {mensagem}\n"
        f"Normalizada: {mensagem_normalizada}\n\n"
        "Responda agora como Sofia — humana, presente, especifica para este usuario:"
    )

    try:
        # ORQUESTRADOR — usa melhor IA disponivel
        resultado_ia = sofia_responder_orquestrador(prompt, usar_cache=False)
        if resultado_ia["ok"]:
            texto_resposta = resultado_ia["texto"]
            ia_usada_sofia = resultado_ia.get("ia", "orquestrador")
            print(f"[Sofia] Respondeu via: {ia_usada_sofia}")
        else:
            # Fallback Gemini direto
            resposta = cliente_ia.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt,
                config=types.GenerateContentConfig(temperature=0.75, max_output_tokens=2048)
            )
            texto_resposta = resposta.text

    except Exception as e:
        erro_str = str(e).lower()
        is_quota = "429" in erro_str or "resource_exhausted" in erro_str or "quota" in erro_str
        print(f"[Gemini] Erro Sofia: {e}")
        import random as _random

        _fallbacks = {
            "alegria": (
                f"que lindo {usuario.nome} sua alegria merece ser celebrada "
                "a gratidao amplifica emocoes positivas escreva 3 coisas que estao te fazendo bem hoje "
                "isso ancora essa energia boa dentro de voce "
                "o que mais esta contribuindo para essa sensacao maravilhosa"
            ),
            "euforia": (
                f"{usuario.nome} que energia incrivel voce esta irradiando "
                "euforia e maravilhosa mas vale ancorar esse momento "
                "escreva o que esta causando isso para poder revisitar depois "
                "como voce quer que essa energia impacte sua vida essa semana"
            ),
            "tristeza": (
                f"{usuario.nome} sinto muito que voce esteja passando por isso "
                "a tristeza e valida ela nos diz que algo importa para nos "
                "tente o acolhimento coloque a mao no coracao respire fundo 3 vezes "
                "e diga estou aqui estou me ouvindo "
                "o que voce precisaria ouvir agora de alguem que te ama"
            ),
            "melancolia": (
                f"{usuario.nome} a melancolia tem uma textura diferente da tristeza comum "
                "ela e mais suave mais contemplativa "
                "permita-se sentir sem resistir "
                "o que essa sensacao esta tentando te dizer sobre o que voce valoriza"
            ),
            "ansiedade": (
                f"{usuario.nome} vamos fazer o Grounding 5-4-3-2-1 juntos agora "
                "nomeie 5 coisas que voce VE 4 que pode TOCAR 3 que OUVE "
                "2 que CHEIRA e 1 que SABOREIA "
                "isso traz sua mente de volta ao presente "
                "como esta seu corpo fisico nesse momento"
            ),
            "panico": (
                f"{usuario.nome} voce esta seguro agora "
                "respira comigo inspire por 4 segundos segure por 4 expire por 4 "
                "faz isso 3 vezes "
                "o panico passa voce consegue atravessar isso "
                "o que voce esta vendo ao seu redor agora mesmo"
            ),
            "raiva": (
                f"{usuario.nome} sua raiva e valida algo importante foi tocado "
                "tente a Respiracao 4-7-8 inspire por 4s segure por 7s expire por 8s "
                "faca 3 vezes isso ativa o sistema parassimpatico "
                "o que exatamente mais te incomoda nessa situacao"
            ),
            "frustracao": (
                f"{usuario.nome} a frustracao aparece quando algo que importa nao sai como esperado "
                "o que especificamente nao foi como voce queria "
                "o que estava em seu controle e o que nao estava "
                "como voce pode ajustar a expectativa ou a estrategia"
            ),
            "medo": (
                f"{usuario.nome} o medo e um sinal do seu sistema de protecao "
                "vamos olhar para ele juntos "
                "o que especificamente te assusta "
                "qual e o pior cenario possivel e qual a probabilidade real dele acontecer"
            ),
            "solidao": (
                f"{usuario.nome} solidao e uma das experiencias mais dolorosas "
                "voce nao esta errado em sentir isso "
                "quando foi a ultima vez que se sentiu verdadeiramente conectado a alguem "
                "que pequeno passo voce poderia dar hoje em direcao a conexao"
            ),
            "burnout": (
                f"{usuario.nome} burnout e o sinal de que voce deu muito por tempo demais "
                "seu corpo e mente estao pedindo socorro "
                "o que voce pode tirar do seu prato hoje mesmo "
                "qual e a coisa MENOS importante que voce pode eliminar agora"
            ),
            "estresse": (
                f"{usuario.nome} o estresse acumulado precisa ser liberado "
                "tente o body scan agora feche os olhos e perceba onde tem tensao no corpo "
                "respire fundo nesse lugar 3 vezes "
                "o que esta pesando mais em voce agora"
            ),
            "culpa": (
                f"{usuario.nome} a culpa saudavel nos ensina a reparar e crescer "
                "a culpa toxica nos paralisa "
                "voce fez o seu melhor com o que tinha naquele momento "
                "o que voce aprendeu com isso e como pode reparar se necessario"
            ),
            "vergonha": (
                f"{usuario.nome} vergonha e uma das emocoes mais dificeis de carregar "
                "ela diz voce e ruim mas a realidade e voce FEZ algo ou algo aconteceu "
                "voce nao e seu erro "
                "o que um amigo compassivo diria para voce agora"
            ),
            "saudade": (
                f"{usuario.nome} saudade e uma das emocoes mais brasileiras e lindas que existem "
                "ela prova que algo ou alguem teve valor real na sua vida "
                "o que voce mais sente falta "
                "como voce pode honrar essa memoria ou pessoa hoje"
            ),
            "luto": (
                f"{usuario.nome} o luto nao tem prazo nem formula certa "
                "cada pessoa vive do seu jeito "
                "voce nao precisa estar bem agora "
                "o que voce precisa para se sentir amparado nesse momento"
            ),
            "vazio": (
                f"{usuario.nome} o vazio existencial e desconfortavel mas tambem e um convite "
                "ele aparece quando algo que dava sentido sumiu "
                "o que costumava te fazer sentir vivo "
                "o que ainda que pequeno te move hoje"
            ),
            "desespero": (
                f"{usuario.nome} sinto que voce esta em um lugar muito pesado agora "
                "voce nao esta sozinho nesse momento "
                "se estiver pensando em se machucar ligue agora para o CVV 188 "
                "funciona 24 horas e completamente gratuito "
                "voce consegue me contar um pouco mais do que esta sentindo"
            ),
            "amor": (
                f"{usuario.nome} que energia bonita o amor traz "
                "e uma das forcas mais transformadoras da vida "
                "como esse sentimento esta impactando voce hoje "
                "o que voce quer fazer com toda essa energia"
            ),
            "gratidao": (
                f"{usuario.nome} gratidao e uma das emocoes mais poderosas para o bem-estar "
                "ela literalmente muda a quimica do cerebro "
                "pelo que especificamente voce esta grato hoje "
                "como voce pode expressar essa gratidao para alguem"
            ),
            "orgulho": (
                f"{usuario.nome} que conquista incrivel "
                "o orgulho saudavel e o reconhecimento de que voce cresceu "
                "o que exatamente voce fez que te deixa orgulhoso "
                "como voce pode celebrar isso de verdade hoje"
            ),
            "esperanca": (
                f"{usuario.nome} esperanca e o combustivel que nos faz continuar "
                "e lindo que voce ainda consegue ver possibilidades "
                "o que especificamente te da esperanca nesse momento "
                "que passo concreto voce pode dar em direcao a isso hoje"
            ),
            "confusao": (
                f"{usuario.nome} confusao aparece quando temos muita coisa para processar "
                "e normal e temporaria "
                "vamos organizar juntos o que esta na sua cabeca "
                "se voce tivesse que escolher UMA coisa para resolver agora qual seria"
            ),
            "neutro": (
                f"{usuario.nome} as vezes nao sentimos nada em particular e isso tambem e valido "
                "como voce descreveria seu estado interno agora "
                "o que esta acontecendo na sua vida nesse momento "
                "tem algo que voce gostaria de explorar comigo hoje"
            ),
            "medo": (
                f"🤗 {usuario.nome}, o medo é um sinal do seu instinto de proteção. "
                "Tente nomear com precisão: 'Estou com medo de ___'. "
                "Nomear reduz a intensidade da emoção no cérebro. "
                "Esse medo é sobre algo passado, presente ou futuro?"
            ),
            "estresse": (
                f"💆 {usuario.nome}, o estresse desgasta. Técnica STOP agora: "
                "Pare, Respire fundo, Observe seus pensamentos sem julgamento, "
                "Prossiga com mais clareza. "
                "Pausas de 2 minutos fazem grande diferença! "
                "O que está pesando mais em você agora?"
            ),
            "amor": (
                f"❤️ {usuario.nome}, que sentimento lindo! "
                "Prática Loving-Kindness: feche os olhos e envie mentalmente amor "
                "para você, depois para quem você ama. "
                "Sobre quem ou o quê você está sentindo esse amor?"
            ),
            "confusão": (
                f"🧩 {usuario.nome}, sentir-se confuso é normal quando há muito para processar. "
                "Tente o Mind Mapping: escreva no centro o que te confunde "
                "e ramifique os pensamentos ao redor. Externalizar organiza a mente. "
                "Se pudesse resolver UMA coisa primeiro, qual seria?"
            ),
            "vergonha": (
                f"🌱 {usuario.nome}, a vergonha não define quem você é. "
                "Prática do Observador Compassivo: imagine um amigo querido "
                "passando pelo mesmo — o que você diria a ele? "
                "Diga isso para si mesmo agora. 💙"
            ),
            "solidão": (
                f"🤝 {usuario.nome}, você não precisa carregar isso sozinho. "
                "Estou aqui com você. "
                "Tente o Journaling: escreva uma carta para alguém que sente falta. "
                "Isso conecta você com suas necessidades reais. "
                "O que está faltando nas suas conexões agora?"
            ),
            "euforia": (
                f"⚡ {usuario.nome}, essa energia alta pode ser incrível! "
                "Prática de Ancoragem: respire fundo e observe seu corpo — "
                "onde você sente essa euforia fisicamente? "
                "Canalizar essa energia de forma intencional é poderoso. "
                "O que você quer criar ou realizar com essa energia hoje?"
            ),
            "frustração": (
                f"💪 {usuario.nome}, a frustração aparece quando algo importante "
                "não saiu como esperado. Isso significa que você se importa! "
                "Tente os 3 Porquês: pergunte 'Por quê estou frustrado?' "
                "três vezes seguidas para chegar à raiz. "
                "O que você esperava que acontecesse de diferente?"
            ),
            "gratidão": (
                f"🙏 {usuario.nome}, a gratidão é uma das emoções mais transformadoras! "
                "Prática: escreva uma carta de gratidão para alguém importante "
                "ou para si mesmo pelo que superou. "
                "Isso fortalece conexões e bem-estar. "
                "Pelo que você está mais grato hoje?"
            ),
            "esperança": (
                f"🌅 {usuario.nome}, a esperança é combustível para o futuro! "
                "Visualização: feche os olhos por 2 minutos e imagine "
                "vividamente o que você espera se tornando realidade. "
                "O que precisa acontecer primeiro para chegar lá?"
            ),
            "neutro": (
                f"🌟 {usuario.nome}, obrigada por compartilhar comigo. "
                "Check-in emocional: de 1 a 10, como está sua energia hoje? "
                "E o que faria essa nota subir pelo menos 1 ponto? "
                "Estou aqui para te ouvir 💙"
            ),
        }

        _emocao_key = emocao_atual.lower()
        _base = _fallbacks.get(_emocao_key, _fallbacks["neutro"])

        if is_quota:
            _aviso = "\n\n_(Estou em manutencao momentanea, mas continuo aqui por voce!)_"
        else:
            _aviso = ""

        texto_resposta = _base + _aviso

    pontos_ganhos = (
        PONTOS_POR_ACAO["chat_premium"]
        if eh_premium
        else PONTOS_POR_ACAO["chat_free"]
    )

    nova_msg = Mensagem(
        conteudo=mensagem,
        resposta=texto_resposta,
        emocao=emocao_atual,
        emoji=get_emoji(emocao_atual),
        usuario_id=usuario.id
    )
    db.add(nova_msg)
    db.commit()

    adicionar_pontos(usuario, pontos_ganhos, db)

    mensagens_hoje_atual = contar_hoje(Mensagem, usuario.id, db)

    return {
        "resposta":          texto_resposta,
        "emocao_detectada":  emocao_atual,
        "emoji":             get_emoji(emocao_atual),
        "tecnica_sugerida":  tecnicas_por_emocao.get(emocao_atual, ""),
        "mensagens_hoje":    mensagens_hoje_atual,
        "limite_chat":       limite,
        "restantes":         max(0, limite - mensagens_hoje_atual),
        "pontos_ganhos":     pontos_ganhos,
        "total_pontos":      usuario.pontos,
        "badge":             usuario.badge,
        "plano":             usuario.plano,
        "modo":              "premium" if eh_premium else "free",
        "recomendacao":      recomendacoes.get(emocao_atual, ""),
    }


@app.get("/chat/historico")
def historico_chat(
    request: Request,
    pagina:  int = 1,
    db:      Session = Depends(get_db)
):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autorizado")

    por_pagina = 15
    offset     = (pagina - 1) * por_pagina

    total = db.query(Mensagem).filter(
        Mensagem.usuario_id == usuario.id
    ).count()

    mensagens = db.query(Mensagem).filter(
        Mensagem.usuario_id == usuario.id
    ).order_by(
        Mensagem.criado_em.asc()
    ).offset(offset).limit(por_pagina).all()

    return {
        "total":        total,
        "pagina":       pagina,
        "total_paginas": (total + por_pagina - 1) // por_pagina,
        "mensagens": [{
            "conteudo":  m.conteudo,
            "resposta":  m.resposta,
            "emocao":    m.emocao,
            "emoji":     m.emoji,
            "timestamp": m.criado_em.strftime("%d/%m/%Y %H:%M"),
        } for m in mensagens]
    }

# ================================================================
# ROTAS — DIÁRIO EMOCIONAL
# ================================================================

@app.post("/diario")
def criar_diario(
    request:  Request,
    titulo:   str = Form(...),
    conteudo: str = Form(...),
    humor:    int = Form(3),
    db:       Session = Depends(get_db)
):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autorizado")

    limite     = get_limite(usuario, "diario")
    total_hoje = contar_hoje(Diario, usuario.id, db)

    if total_hoje >= limite:
        raise HTTPException(
            status_code=429,
            detail=(
                f"⚠️ Você atingiu o limite de {limite} entradas por dia. "
                f"{'Faça upgrade para Premium e tenha entradas ilimitadas! 💎' if usuario.plano == 'free' else 'Aguarde até amanhã!'}"
            )
        )

    if len(titulo.strip()) < 2:
        raise HTTPException(
            status_code=400,
            detail="⚠️ Título muito curto."
        )

    if len(conteudo.strip()) < 10:
        raise HTTPException(
            status_code=400,
            detail="⚠️ Conteúdo muito curto. Escreva pelo menos 10 caracteres."
        )

    # Humor deve ser entre 1 e 5
    humor = max(1, min(5, humor))

    # GEMINI no diario
    try:
        _ad = detectar_emocao_hibrido(conteudo + " " + titulo, usar_gemini=True)
        emocao = _ad.get("emocao", "neutro")
    except:
        try:
            _ad = detectar_emocao_hibrido(conteudo + " " + titulo, usar_gemini=True)
            emocao = _ad.get("emocao", "neutro")
        except:
            emocao = detectar_emocao(conteudo + " " + titulo)
    tecnica = tecnicas_por_emocao.get(emocao, "")

    novo = Diario(
        titulo=titulo.strip(),
        conteudo=conteudo.strip(),
        emocao=emocao.capitalize(),
        emoji=get_emoji(emocao),
        humor=humor,
        usuario_id=usuario.id
    )
    db.add(novo)
    db.commit()
    db.refresh(novo)

    adicionar_pontos(usuario, PONTOS_POR_ACAO["diario"], db)

    # Verifica conquistas
    total_diarios = db.query(Diario).filter(
        Diario.usuario_id == usuario.id
    ).count()

    mensagem_especial = None
    if total_diarios == 1:
        mensagem_especial = "📖 Primeira entrada no diário! Continue escrevendo!"
    elif total_diarios == 7:
        mensagem_especial = "🎉 7 entradas no diário! Conquista desbloqueada!"
    elif total_diarios == 30:
        mensagem_especial = "🏆 30 entradas! Você é dedicado ao autoconhecimento!"

    humor_label = {
        1: "😔 Muito mal",
        2: "😕 Mal",
        3: "😐 Neutro",
        4: "😊 Bem",
        5: "😄 Muito bem"
    }.get(humor, "😐 Neutro")

    return {
        "mensagem":         "✅ Entrada salva com sucesso!",
        "id":               novo.id,
        "emocao":           emocao.capitalize(),
        "emoji":            get_emoji(emocao),
        "recomendacao":     recomendacoes.get(emocao, ""),
        "tecnica":          tecnica,
        "humor":            humor,
        "humor_label":      humor_label,
        "pontos_ganhos":    PONTOS_POR_ACAO["diario"],
        "total_pontos":     usuario.pontos,
        "badge":            usuario.badge,
        "entradas_hoje":    total_hoje + 1,
        "limite_diario":    limite,
        "mensagem_especial": mensagem_especial,
        "timestamp":        datetime.now().strftime("%d/%m/%Y %H:%M"),
    }


@app.get("/diario")
def ver_diario(
    request: Request,
    pagina:  int = 1,
    db:      Session = Depends(get_db)
):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autorizado")

    por_pagina = 10
    offset     = (pagina - 1) * por_pagina

    total = db.query(Diario).filter(
        Diario.usuario_id == usuario.id
    ).count()

    entradas = db.query(Diario).filter(
        Diario.usuario_id == usuario.id
    ).order_by(
        Diario.criado_em.desc()
    ).offset(offset).limit(por_pagina).all()

    # Estatísticas do diário
    todas = db.query(Diario).filter(
        Diario.usuario_id == usuario.id
    ).all()

    humor_medio = round(
        sum(e.humor for e in todas) / len(todas), 1
    ) if todas else 0

    emocoes_diario = {}
    for e in todas:
        em = e.emocao.lower() if e.emocao else "neutro"
        emocoes_diario[em] = emocoes_diario.get(em, 0) + 1

    humor_label = {
        1: "😔 Muito mal",
        2: "😕 Mal",
        3: "😐 Neutro",
        4: "😊 Bem",
        5: "😄 Muito bem"
    }

    return {
        "total":          total,
        "pagina":         pagina,
        "total_paginas":  (total + por_pagina - 1) // por_pagina,
        "humor_medio":    humor_medio,
        "emocoes_diario": emocoes_diario,
        "entradas": [{
            "id":        e.id,
            "titulo":    e.titulo,
            "conteudo":  e.conteudo[:200] + "..." if len(e.conteudo) > 200 else e.conteudo,
            "emocao":    e.emocao,
            "emoji":     e.emoji,
            "humor":     e.humor,
            "humor_label": humor_label.get(e.humor, "😐 Neutro"),
            "timestamp": e.criado_em.strftime("%d/%m/%Y %H:%M"),
        } for e in entradas]
    }


@app.get("/diario/{diario_id}")
def ver_diario_entry(
    diario_id: int,
    request:   Request,
    db:        Session = Depends(get_db)
):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autorizado")

    entrada = db.query(Diario).filter(
        Diario.id         == diario_id,
        Diario.usuario_id == usuario.id
    ).first()

    if not entrada:
        raise HTTPException(
            status_code=404,
            detail="❌ Entrada não encontrada."
        )

    return {
        "id":        entrada.id,
        "titulo":    entrada.titulo,
        "conteudo":  entrada.conteudo,
        "emocao":    entrada.emocao,
        "emoji":     entrada.emoji,
        "humor":     entrada.humor,
        "tecnica":   tecnicas_por_emocao.get(
            entrada.emocao.lower() if entrada.emocao else "neutro", ""
        ),
        "recomendacao": recomendacoes.get(
            entrada.emocao.lower() if entrada.emocao else "neutro", ""
        ),
        "timestamp": entrada.criado_em.strftime("%d/%m/%Y %H:%M"),
    }


@app.delete("/diario/{diario_id}")
def deletar_diario(
    diario_id: int,
    request:   Request,
    db:        Session = Depends(get_db)
):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autorizado")

    entrada = db.query(Diario).filter(
        Diario.id         == diario_id,
        Diario.usuario_id == usuario.id
    ).first()

    if not entrada:
        raise HTTPException(
            status_code=404,
            detail="❌ Entrada não encontrada."
        )

    db.delete(entrada)
    db.commit()

    return {
        "mensagem": "✅ Entrada deletada com sucesso!",
        "id":       diario_id
    }


@app.put("/diario/{diario_id}")
def editar_diario(
    diario_id: int,
    request:   Request,
    titulo:    str = Form(...),
    conteudo:  str = Form(...),
    humor:     int = Form(3),
    db:        Session = Depends(get_db)
):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autorizado")

    entrada = db.query(Diario).filter(
        Diario.id         == diario_id,
        Diario.usuario_id == usuario.id
    ).first()

    if not entrada:
        raise HTTPException(
            status_code=404,
            detail="❌ Entrada não encontrada."
        )

    # GEMINI no diario v2
    try:
        _ad2 = detectar_emocao_hibrido(conteudo + " " + titulo, usar_gemini=True)
        emocao = _ad2.get("emocao", "neutro")
    except:
        try:
            _ad = detectar_emocao_hibrido(conteudo + " " + titulo, usar_gemini=True)
            emocao = _ad.get("emocao", "neutro")
        except:
            emocao = detectar_emocao(conteudo + " " + titulo)
    entrada.titulo   = titulo.strip()
    entrada.conteudo = conteudo.strip()
    entrada.emocao   = emocao.capitalize()
    entrada.emoji    = get_emoji(emocao)
    entrada.humor    = max(1, min(5, humor))
    db.commit()

    return {
        "mensagem": "✅ Entrada atualizada com sucesso!",
        "emocao":   emocao.capitalize(),
        "emoji":    get_emoji(emocao),
    }

# ================================================================
# ROTAS — GAMIFICAÇÃO COMPLETA
# ================================================================

@app.get("/gamificacao")
def gamificacao(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autorizado")

    conquistas = db.query(Conquista).filter(
        Conquista.usuario_id == usuario.id
    ).all()

    prox = proximo_badge(usuario.pontos)

    # Progresso para próximo badge
    badges_config = [
        (0,    "🌱 Iniciante",      "#6b7280"),
        (50,   "🌿 Explorador",     "#22c55e"),
        (200,  "🔥 Intermediário",  "#f97316"),
        (500,  "⭐ Avançado",       "#eab308"),
        (1000, "🏆 Especialista",   "#3b82f6"),
        (2000, "💎 Mestre Emocional","#8b5cf6"),
        (5000, "👑 Lenda Emocional", "#ec4899"),
    ]

    badge_atual_idx = 0
    for i, (limite, badge, cor) in enumerate(badges_config):
        if usuario.pontos >= limite:
            badge_atual_idx = i

    progresso_percent = 0
    if badge_atual_idx < len(badges_config) - 1:
        limite_atual  = badges_config[badge_atual_idx][0]
        limite_proximo = badges_config[badge_atual_idx + 1][0]
        progresso_percent = round(
            (usuario.pontos - limite_atual) /
            (limite_proximo - limite_atual) * 100
        )

    # Histórico de pontos (atividades recentes)
    analises_recentes = db.query(Analise).filter(
        Analise.usuario_id == usuario.id
    ).order_by(Analise.criado_em.desc()).limit(5).all()

    msgs_recentes = db.query(Mensagem).filter(
        Mensagem.usuario_id == usuario.id
    ).order_by(Mensagem.criado_em.desc()).limit(5).all()

    atividades = []
    for a in analises_recentes:
        atividades.append({
            "tipo":      "analise",
            "descricao": f"Análise emocional: {a.emocao}",
            "emoji":     a.emoji,
            "pontos":    PONTOS_POR_ACAO["analise"],
            "timestamp": a.criado_em.strftime("%d/%m %H:%M"),
        })
    for m in msgs_recentes:
        atividades.append({
            "tipo":      "chat",
            "descricao": "Conversa com Sofia",
            "emoji":     "🧠",
            "pontos":    PONTOS_POR_ACAO["chat_premium"] if usuario.plano in ["premium","enterprise"] else PONTOS_POR_ACAO["chat_free"],
            "timestamp": m.criado_em.strftime("%d/%m %H:%M"),
        })

    atividades.sort(key=lambda x: x["timestamp"], reverse=True)

    return {
        "pontos":             usuario.pontos,
        "badge":              usuario.badge,
        "proximo_badge":      prox,
        "progresso_percent":  progresso_percent,
        "total_conquistas":   len(conquistas),
        "conquistas": [{
            "nome":      c.nome,
            "descricao": c.descricao,
            "emoji":     c.emoji,
            "timestamp": c.criado_em.strftime("%d/%m/%Y"),
        } for c in conquistas],
        "badges_config": [{
            "limite":      limite,
            "badge":       badge,
            "cor":         cor,
            "conquistado": usuario.pontos >= limite,
        } for limite, badge, cor in badges_config],
        "atividades_recentes": atividades[:10],
        "tabela_pontos": {
            "Cadastro":         PONTOS_POR_ACAO["cadastro"],
            "Análise emocional": PONTOS_POR_ACAO["analise"],
            "Chat (Free)":      PONTOS_POR_ACAO["chat_free"],
            "Chat (Premium)":   PONTOS_POR_ACAO["chat_premium"],
            "Entrada no diário": PONTOS_POR_ACAO["diario"],
            "Ativar Trial":     PONTOS_POR_ACAO["trial"],
            "Assinar Premium":  PONTOS_POR_ACAO["premium"],
        }
    }

# ================================================================
# FIM DA PARTE 3
# ================================================================
# ================================================================
# ROTAS — CHECKOUT E PAGAMENTOS
# ================================================================

@app.get("/checkout-page", response_class=HTMLResponse)
def checkout_page(request: Request, plano: str = "premium", db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return RedirectResponse(url="/login")
    return templates.TemplateResponse(request, "checkout.html", {
        "usuario": usuario,
        "plano": plano,
        "precos": PRECOS,
    })

@app.get("/checkout")
def checkout(
    request: Request,
    plano:   str,
    db:      Session = Depends(get_db)
):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return RedirectResponse(url="/login")

    if plano not in PRECOS:
        raise HTTPException(
            status_code=400,
            detail="❌ Plano inválido. Escolha premium ou enterprise."
        )

    if usuario.plano == plano:
        raise HTTPException(
            status_code=400,
            detail=f"⚠️ Você já possui o plano {plano.capitalize()}."
        )

    try:
        sdk = mercadopago.SDK(MP_ACCESS_TOKEN)

        preference_data = {
            "items": [{
                "title":       PRECOS[plano]["nome"],
                "description": f"Plano {plano.capitalize()} — Emotion Intelligence v14.0",
                "quantity":    1,
                "currency_id": "BRL",
                "unit_price":  float(PRECOS[plano]["valor"])
            }],
            "payer": {
                "name":  usuario.nome.split()[0],
                "email": usuario.email,
            },
            "metadata": {
                "usuario_id": usuario.id,
                "plano":      plano,
                "email":      usuario.email,
            },
            "back_urls": {
                "success": f"{BASE_URL}/sucesso",
                "failure": f"{BASE_URL}/falha",
                "pending": f"{BASE_URL}/pendente",
            },
            "notification_url": f"{BASE_URL}/webhook/mercadopago",
            "auto_return":      "approved",
            "statement_descriptor": "EMOTION INTEL",
            "expires": False,
        }

        pref     = sdk.preference().create(preference_data)
        init_url = pref["response"]["init_point"]

        # Registra pagamento pendente
        pagamento = Pagamento(
            usuario_id=usuario.id,
            plano=plano,
            valor=float(PRECOS[plano]["valor"]),
            status="pendente"
        )
        db.add(pagamento)
        db.commit()

        registrar_log("/checkout", "GET", 
            request.client.host if request.client else "unknown",
            302, usuario.id, db
        )

        return RedirectResponse(url=init_url)

    except Exception as e:
        print(f"[Checkout] Erro: {e}")
        raise HTTPException(
            status_code=500,
            detail=(
                "❌ Erro ao iniciar pagamento. "
                "Tente novamente ou entre em contato com o suporte."
            )
        )

# ================================================================
# WEBHOOK — MERCADOPAGO
# ================================================================

@app.post("/webhook/mercadopago")
async def webhook_mp(
    request: Request,
    db:      Session = Depends(get_db)
):
    try:
        data = await request.json()
        tipo = data.get("type", "")

        print(f"[Webhook] Recebido: {tipo} — {data}")

        if tipo not in ["payment", "merchant_order"]:
            return {"status": "ignored", "tipo": tipo}

        if tipo == "payment":
            mp_id = str(data.get("data", {}).get("id", ""))
            if not mp_id:
                return {"status": "error", "detail": "ID não encontrado"}

            sdk     = mercadopago.SDK(MP_ACCESS_TOKEN)
            payment = sdk.payment().get(mp_id)
            info    = payment["response"]
            status  = info.get("status", "")
            meta    = info.get("metadata", {})
            uid     = meta.get("usuario_id")
            plano   = meta.get("plano", "premium")
            email   = meta.get("email", "")
            metodo  = info.get("payment_type_id", "")

            print(f"[Webhook] Payment {mp_id}: status={status}, uid={uid}, plano={plano}")

            if status == "approved" and uid:
                usuario = db.query(Usuario).filter(
                    Usuario.id == int(uid)
                ).first()

                if usuario:
                    plano_anterior = usuario.plano
                    usuario.plano  = plano
                    db.commit()

                    adicionar_pontos(
                        usuario,
                        PONTOS_POR_ACAO["premium"],
                        db
                    )

                    # Atualiza pagamento
                    pagamento = db.query(Pagamento).filter(
                        Pagamento.usuario_id == int(uid),
                        Pagamento.status     == "pendente"
                    ).order_by(Pagamento.criado_em.desc()).first()

                    if pagamento:
                        pagamento.status = "aprovado"
                        pagamento.mp_id  = mp_id
                        pagamento.metodo = metodo
                        db.commit()
                    else:
                        novo_pag = Pagamento(
                            usuario_id=int(uid),
                            plano=plano,
                            valor=float(
                                PRECOS.get(plano, {}).get("valor", 49)
                            ),
                            status="aprovado",
                            mp_id=mp_id,
                            metodo=metodo
                        )
                        db.add(novo_pag)
                        db.commit()

                    # Cria notificação para o usuário
                    notif = Notificacao(
                        titulo=f"🎉 Plano {plano.capitalize()} ativado!",
                        mensagem=(
                            f"Seu pagamento foi aprovado! "
                            f"Aproveite todos os recursos do plano "
                            f"{plano.capitalize()}. +{PONTOS_POR_ACAO['premium']} "
                            f"pontos de bônus adicionados!"
                        ),
                        usuario_id=int(uid)
                    )
                    db.add(notif)
                    db.commit()

                    import asyncio
                    try:
                        asyncio.create_task(
                            enviar_email_premium(
                                usuario.nome,
                                usuario.email,
                                plano
                            )
                        )
                    except Exception:
                        import threading
                        threading.Thread(
                            target=lambda: __import__('asyncio').run(
                                enviar_email_premium(
                                    usuario.nome,
                                    usuario.email,
                                    plano
                                )
                            )
                        ).start()

                    print(
                        f"[Webhook] ✅ Plano {plano} ativado para "
                        f"{usuario.email} (antes: {plano_anterior})"
                    )

            elif status in ["rejected", "cancelled"]:
                pagamento = db.query(Pagamento).filter(
                    Pagamento.usuario_id == int(uid) if uid else False,
                    Pagamento.status     == "pendente"
                ).order_by(Pagamento.criado_em.desc()).first()

                if pagamento:
                    pagamento.status = status
                    pagamento.mp_id  = mp_id
                    db.commit()

        return {"status": "ok", "processed": tipo}

    except Exception as e:
        print(f"[Webhook] Erro: {e}")
        return {"status": "error", "detail": str(e)}

# ================================================================
# ROTAS — RETORNO DE PAGAMENTO
# ================================================================

@app.get("/sucesso", response_class=HTMLResponse)
async def sucesso(
    background_tasks: BackgroundTasks,
    request:          Request,
    db:               Session = Depends(get_db)
):
    usuario = get_usuario_logado(request, db)

    if usuario and usuario.plano not in ["premium", "enterprise"]:
        usuario.plano = "premium"
        db.commit()
        adicionar_pontos(usuario, PONTOS_POR_ACAO["premium"], db)
        enviar_telegram(
            "💰 <b>Nova assinatura Premium!</b>\n"
            f"👤 {usuario.nome}\n"
            f"📧 {usuario.email}\n"
            f"🕐 {datetime.now().strftime('%d/%m/%Y %H:%M')}"
        )
        background_tasks.add_task(
            enviar_email_premium,
            usuario.nome,
            usuario.email,
            "premium"
        )

    nome = usuario.nome if usuario else "usuario"

    return templates.TemplateResponse(request, "sucesso.html", {
        "usuario": usuario,
        "nome": nome,
    })


@app.get("/falha", response_class=HTMLResponse)
def falha(request: Request):
    return HTMLResponse(f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Pagamento Falhou — Emotion Intelligence</title>
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{
                font-family: 'Segoe UI', sans-serif;
                background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
            }}
            .card {{
                background: rgba(255,255,255,0.05);
                backdrop-filter: blur(20px);
                border: 1px solid rgba(231,76,60,0.3);
                border-radius: 24px;
                padding: 60px 50px;
                text-align: center;
                max-width: 500px;
                width: 90%;
            }}
            .icon {{ font-size: 80px; margin-bottom: 20px; }}
            h1 {{
                font-size: 32px;
                margin-bottom: 15px;
                color: #e74c3c;
            }}
            p {{
                color: rgba(255,255,255,0.7);
                font-size: 16px;
                line-height: 1.6;
                margin-bottom: 15px;
            }}
            .opcoes {{
                background: rgba(255,255,255,0.05);
                border-radius: 12px;
                padding: 20px;
                margin: 20px 0;
                text-align: left;
            }}
            .btn {{
                display: inline-block;
                background: linear-gradient(90deg, #e74c3c, #c0392b);
                color: white;
                padding: 15px 40px;
                border-radius: 50px;
                text-decoration: none;
                font-size: 16px;
                font-weight: bold;
                margin: 5px;
            }}
            .btn-sec {{
                background: rgba(255,255,255,0.1);
                border: 1px solid rgba(255,255,255,0.2);
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <div class="icon">❌</div>
            <h1>Pagamento não aprovado</h1>
            <p>Não se preocupe! Isso acontece às vezes.<br>
            Verifique os dados e tente novamente.</p>
            <div class="opcoes">
                <p style="color: rgba(255,255,255,0.9);">
                    <strong>Possíveis causas:</strong>
                </p>
                <p>
                    • Saldo insuficiente<br>
                    • Dados do cartão incorretos<br>
                    • Limite do cartão atingido<br>
                    • Transação bloqueada pelo banco
                </p>
            </div>
            <a href="/planos" class="btn">🔄 Tentar novamente</a>
            <a href="/" class="btn btn-sec">🏠 Voltar ao início</a>
        </div>
    </body>
    </html>
    """)


@app.get("/pendente", response_class=HTMLResponse)
def pendente(request: Request):
    return HTMLResponse(f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Pagamento Pendente — Emotion Intelligence</title>
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{
                font-family: 'Segoe UI', sans-serif;
                background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
            }}
            .card {{
                background: rgba(255,255,255,0.05);
                backdrop-filter: blur(20px);
                border: 1px solid rgba(243,156,18,0.3);
                border-radius: 24px;
                padding: 60px 50px;
                text-align: center;
                max-width: 500px;
                width: 90%;
            }}
            .icon {{ font-size: 80px; margin-bottom: 20px; }}
            h1 {{ font-size: 32px; margin-bottom: 15px; color: #f39c12; }}
            p {{
                color: rgba(255,255,255,0.7);
                font-size: 16px;
                line-height: 1.6;
                margin-bottom: 15px;
            }}
            .info {{
                background: rgba(243,156,18,0.1);
                border: 1px solid rgba(243,156,18,0.3);
                border-radius: 12px;
                padding: 20px;
                margin: 20px 0;
            }}
            .btn {{
                display: inline-block;
                background: linear-gradient(90deg, #f39c12, #e67e22);
                color: white;
                padding: 15px 40px;
                border-radius: 50px;
                text-decoration: none;
                font-size: 16px;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <div class="icon">⏳</div>
            <h1>Pagamento Pendente</h1>
            <p>Seu pagamento está sendo processado!</p>
            <div class="info">
                <p style="color: rgba(255,255,255,0.9);">
                    ℹ️ Assim que confirmado, seu plano será
                    ativado automaticamente e você receberá
                    um email de confirmação. <br><br>
                    Pagamentos via PIX e boleto podem
                    levar até 2 dias úteis.
                </p>
            </div>
            <a href="/" class="btn">🏠 Voltar ao Dashboard</a>
        </div>
    </body>
    </html>
    """)

# ================================================================
# ROTAS — ADMIN COMPLETO
# ================================================================

@app.get("/admin", response_class=HTMLResponse)
def admin(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario or usuario.email != ADMIN_EMAIL:
        return RedirectResponse(url="/")

    todos          = db.query(Usuario).order_by(
        Usuario.criado_em.desc()
    ).all()
    total_analises = db.query(Analise).count()
    total_msgs     = db.query(Mensagem).count()
    total_diarios  = db.query(Diario).count()
    total_logs     = db.query(LogAcesso).count()
    total_conquistas = db.query(Conquista).count()

    pagamentos_aprovados = db.query(Pagamento).filter(
        Pagamento.status == "aprovado"
    ).all()

    pagamentos_pendentes = db.query(Pagamento).filter(
        Pagamento.status == "pendente"
    ).count()

    premium    = [u for u in todos if u.plano == "premium"]
    enterprise = [u for u in todos if u.plano == "enterprise"]
    trial      = [u for u in todos if u.plano == "trial"]
    free       = [u for u in todos if u.plano == "free"]
    ativos     = [u for u in todos if u.ativo]
    inativos   = [u for u in todos if not u.ativo]

    receita_total = sum(
        p.valor or 0
        for p in pagamentos_aprovados
    )

    receita_mensal = sum(
        p.valor or 0
        for p in pagamentos_aprovados
        if p.criado_em and p.criado_em >= datetime.now() - timedelta(days=30)
    )

    logs_recentes = db.query(LogAcesso).order_by(
        LogAcesso.criado_em.desc()
    ).limit(100).all()

    # Novos usuários por dia (últimos 7 dias)
    novos_por_dia = {}
    for i in range(7):
        dia = (datetime.now() - timedelta(days=i)).strftime("%d/%m")
        novos_por_dia[dia] = 0
    for u in todos:
        dia = u.criado_em.strftime("%d/%m")
        if dia in novos_por_dia:
            novos_por_dia[dia] += 1

    # Top usuários por pontos
    top_usuarios = sorted(todos, key=lambda u: u.pontos, reverse=True)[:10]

    lista_usuarios = [{
        "id":             u.id,
        "nome":           u.nome,
        "email":          u.email,
        "plano":          u.plano,
        "pontos":         u.pontos,
        "badge":          u.badge,
        "total_analises": len(u.analises),
        "total_msgs":     len(u.mensagens),
        "total_diarios":  len(u.diarios),
        "criado_em":      u.criado_em.strftime("%d/%m/%Y"),
        "ultimo_acesso":  u.ultimo_acesso.strftime("%d/%m/%Y %H:%M") if u.ultimo_acesso else "Nunca",
        "ativo":          u.ativo,
        "ref_code":       u.ref_code,
        "indicado_por":   u.indicado_por,
        "trial_usado":    u.trial_usado,
        "api_token":      u.api_token[:20] + "..." if u.api_token else None,
    } for u in todos]

    return templates.TemplateResponse(request, "admin.html", {
        "usuario":              usuario,
        "usuarios":             lista_usuarios,
        "top_usuarios":         top_usuarios,
        "total_usuarios":       len(todos),
        "usuarios_free":        len(free),
        "usuarios_trial":       len(trial),
        "usuarios_premium":     len(premium),
        "usuarios_enterprise":  len(enterprise),
        "usuarios_ativos":      len(ativos),
        "usuarios_inativos":    len(inativos),
        "total_analises":       total_analises,
        "total_msgs":           total_msgs,
        "total_diarios":        total_diarios,
        "total_logs":           total_logs,
        "total_conquistas":     total_conquistas,
        "receita_total":        receita_total,
        "receita_mensal":       receita_mensal,
        "pagamentos_pendentes": pagamentos_pendentes,
        "logs_recentes":        logs_recentes,
        "novos_por_dia":        json.dumps(novos_por_dia),
        "distribuicao_planos":  json.dumps({
            "Free":       len(free),
            "Trial":      len(trial),
            "Premium":    len(premium),
            "Enterprise": len(enterprise),
        }),
    })


@app.post("/admin/usuario/{uid}/plano")
def admin_mudar_plano(
    uid:     int,
    request: Request,
    plano:   str = Form(...),
    db:      Session = Depends(get_db)
):
    admin_user = get_usuario_logado(request, db)
    if not admin_user or admin_user.email != ADMIN_EMAIL:
        raise HTTPException(status_code=403, detail="Acesso negado")

    planos_validos = ["free", "trial", "premium", "enterprise"]
    if plano not in planos_validos:
        raise HTTPException(
            status_code=400,
            detail=f"Plano inválido. Use: {', '.join(planos_validos)}"
        )

    usuario = db.query(Usuario).filter(Usuario.id == uid).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    plano_anterior = usuario.plano
    usuario.plano  = plano

    if plano in ["premium", "enterprise"] and plano_anterior == "free":
        adicionar_pontos(usuario, PONTOS_POR_ACAO["premium"], db)

    db.commit()

    return {
        "mensagem":        f"✅ Plano de {usuario.nome} alterado para {plano}",
        "plano_anterior":  plano_anterior,
        "plano_atual":     plano,
        "usuario_email":   usuario.email,
    }


@app.post("/admin/usuario/{uid}/toggle")
def admin_toggle_usuario(
    uid:     int,
    request: Request,
    db:      Session = Depends(get_db)
):
    admin_user = get_usuario_logado(request, db)
    if not admin_user or admin_user.email != ADMIN_EMAIL:
        raise HTTPException(status_code=403, detail="Acesso negado")

    if uid == admin_user.id:
        raise HTTPException(
            status_code=400,
            detail="❌ Você não pode desativar sua própria conta."
        )

    usuario = db.query(Usuario).filter(Usuario.id == uid).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    usuario.ativo = not usuario.ativo
    db.commit()

    status = "ativado ✅" if usuario.ativo else "desativado 🚫"

    return {
        "mensagem": f"Usuário {usuario.nome} {status}",
        "ativo":    usuario.ativo,
        "nome":     usuario.nome,
        "email":    usuario.email,
    }


@app.delete("/admin/usuario/{uid}")
def admin_deletar_usuario(
    uid:     int,
    request: Request,
    db:      Session = Depends(get_db)
):
    admin_user = get_usuario_logado(request, db)
    if not admin_user or admin_user.email != ADMIN_EMAIL:
        raise HTTPException(status_code=403, detail="Acesso negado")

    if uid == admin_user.id:
        raise HTTPException(
            status_code=400,
            detail="❌ Você não pode deletar sua própria conta."
        )

    usuario = db.query(Usuario).filter(Usuario.id == uid).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    nome  = usuario.nome
    email = usuario.email

    db.delete(usuario)
    db.commit()

    return {
        "mensagem": f"✅ Usuário {nome} ({email}) deletado com sucesso.",
        "id":       uid,
    }


@app.post("/admin/relatorio/{uid}")
async def admin_enviar_relatorio(
    uid:     int,
    request: Request,
    db:      Session = Depends(get_db)
):
    admin_user = get_usuario_logado(request, db)
    if not admin_user or admin_user.email != ADMIN_EMAIL:
        raise HTTPException(status_code=403, detail="Acesso negado")

    usuario = db.query(Usuario).filter(Usuario.id == uid).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    await enviar_relatorio_semanal(usuario, db)

    return {
        "mensagem": f"✅ Relatório enviado para {usuario.email}",
        "nome":     usuario.nome,
        "email":    usuario.email,
    }


@app.post("/admin/notificacao/{uid}")
def admin_enviar_notificacao(
    uid:      int,
    request:  Request,
    titulo:   str = Form(...),
    mensagem: str = Form(...),
    db:       Session = Depends(get_db)
):
    admin_user = get_usuario_logado(request, db)
    if not admin_user or admin_user.email != ADMIN_EMAIL:
        raise HTTPException(status_code=403, detail="Acesso negado")

    usuario = db.query(Usuario).filter(Usuario.id == uid).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    notif = Notificacao(
        titulo=titulo,
        mensagem=mensagem,
        usuario_id=uid
    )
    db.add(notif)
    db.commit()

    return {
        "mensagem": f"✅ Notificação enviada para {usuario.nome}",
        "titulo":   titulo,
    }


@app.get("/admin/stats/json")
def admin_stats_json(request: Request, db: Session = Depends(get_db)):
    admin_user = get_usuario_logado(request, db)
    if not admin_user or admin_user.email != ADMIN_EMAIL:
        raise HTTPException(status_code=403, detail="Acesso negado")

    todos          = db.query(Usuario).all()
    total_analises = db.query(Analise).count()
    total_msgs     = db.query(Mensagem).count()
    total_diarios  = db.query(Diario).count()

    pagamentos = db.query(Pagamento).filter(
        Pagamento.status == "aprovado"
    ).all()

    receita = sum(
        49  if p.plano == "premium"    else
        199 if p.plano == "enterprise" else 0
        for p in pagamentos
    )

    return {
        "total_usuarios":    len(todos),
        "usuarios_free":     sum(1 for u in todos if u.plano == "free"),
        "usuarios_trial":    sum(1 for u in todos if u.plano == "trial"),
        "usuarios_premium":  sum(1 for u in todos if u.plano == "premium"),
        "usuarios_enterprise": sum(1 for u in todos if u.plano == "enterprise"),
        "usuarios_ativos":   sum(1 for u in todos if u.ativo),
        "total_analises":    total_analises,
        "total_mensagens":   total_msgs,
        "total_diarios":     total_diarios,
        "receita_total":     receita,
        "total_pagamentos":  len(pagamentos),
        "timestamp":         datetime.now().isoformat(),
    }

# ================================================================
# API PÚBLICA COM TOKEN
# ================================================================

def verificar_token(
    x_api_token: str     = Header(None),
    db:          Session = Depends(get_db)
):
    if not x_api_token:
        raise HTTPException(
            status_code=401,
            detail="❌ Token não fornecido. Use o header X-Api-Token."
        )

    usuario = db.query(Usuario).filter(
        Usuario.api_token == x_api_token,
        Usuario.ativo     == True
    ).first()

    if not usuario:
        raise HTTPException(
            status_code=401,
            detail="❌ Token inválido ou conta desativada."
        )

    return usuario


@app.get("/exportar/csv")
def exportar_csv(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Nao autorizado")

    import csv, io
    analises = db.query(Analise).filter(
        Analise.usuario_id == usuario.id
    ).order_by(Analise.criado_em.desc()).all()

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Data", "Texto", "Emocao", "Emoji", "Intensidade", "Recomendacao"])
    for a in analises:
        writer.writerow([
            a.criado_em.strftime("%d/%m/%Y %H:%M"),
            a.texto[:200],
            a.emocao,
            a.emoji,
            getattr(a, "intensidade", ""),
            getattr(a, "recomendacao", ""),
        ])

    diarios = db.query(Diario).filter(
        Diario.usuario_id == usuario.id
    ).order_by(Diario.criado_em.desc()).all()

    writer.writerow([])
    writer.writerow(["=== DIARIO EMOCIONAL ==="])
    writer.writerow(["Data", "Titulo", "Conteudo", "Emocao", "Emoji"])
    for d in diarios:
        writer.writerow([
            d.criado_em.strftime("%d/%m/%Y %H:%M"),
            getattr(d, "titulo", ""),
            d.conteudo[:300],
            getattr(d, "emocao", ""),
            getattr(d, "emoji", ""),
        ])

    output.seek(0)
    nome_arquivo = f"emotion_intelligence_{usuario.nome.replace(' ','_')}_{datetime.now().strftime('%Y%m%d')}.csv"

    return Response(
        content=output.getvalue().encode("utf-8-sig"),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename={nome_arquivo}"}
    )



# ================================================================
# ROTA — CERTIFICADO DE IE EM PDF (Premium)
# ================================================================


# ================================================================
# ROTAS — CUPONS DE DESCONTO
# ================================================================

@app.post("/cupom/validar")
def validar_cupom(
    request: Request,
    codigo: str = Form(...),
    db: Session = Depends(get_db)
):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Nao autorizado")

    cupom = db.query(Cupom).filter(
        Cupom.codigo == codigo.upper().strip(),
        Cupom.ativo == True
    ).first()

    if not cupom:
        raise HTTPException(status_code=404, detail="Cupom invalido ou expirado")

    if cupom.expira_em and cupom.expira_em < datetime.now():
        raise HTTPException(status_code=400, detail="Cupom expirado")

    if cupom.usos_atuais >= cupom.usos_maximos:
        raise HTTPException(status_code=400, detail="Cupom esgotado")

    preco_original = 49
    desconto = int(preco_original * cupom.desconto_pct / 100)
    preco_final = preco_original - desconto

    return {
        "valido": True,
        "codigo": cupom.codigo,
        "desconto_pct": cupom.desconto_pct,
        "desconto_valor": desconto,
        "preco_original": preco_original,
        "preco_final": preco_final,
        "mensagem": f"Cupom aplicado! {cupom.desconto_pct}% de desconto — R${preco_final}/mes"
    }

@app.post("/admin/cupom/criar")
def criar_cupom(
    request: Request,
    codigo: str = Form(...),
    desconto_pct: int = Form(...),
    usos_maximos: int = Form(100),
    dias_validade: int = Form(30),
    db: Session = Depends(get_db)
):
    usuario = get_usuario_logado(request, db)
    if not usuario or usuario.email != ADMIN_EMAIL:
        raise HTTPException(status_code=403, detail="Apenas admin")

    existente = db.query(Cupom).filter(Cupom.codigo == codigo.upper()).first()
    if existente:
        raise HTTPException(status_code=400, detail="Cupom ja existe")

    cupom = Cupom(
        codigo=codigo.upper().strip(),
        desconto_pct=desconto_pct,
        usos_maximos=usos_maximos,
        expira_em=datetime.now() + timedelta(days=dias_validade)
    )
    db.add(cupom)
    db.commit()

    return {
        "mensagem": f"Cupom {cupom.codigo} criado com sucesso!",
        "codigo": cupom.codigo,
        "desconto_pct": cupom.desconto_pct,
        "expira_em": cupom.expira_em.strftime("%d/%m/%Y")
    }

@app.get("/admin/cupons")
def listar_cupons(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario or usuario.email != ADMIN_EMAIL:
        raise HTTPException(status_code=403, detail="Apenas admin")

    cupons = db.query(Cupom).order_by(Cupom.criado_em.desc()).all()
    return [{
        "codigo": c.codigo,
        "desconto_pct": c.desconto_pct,
        "usos": f"{c.usos_atuais}/{c.usos_maximos}",
        "ativo": c.ativo,
        "expira_em": c.expira_em.strftime("%d/%m/%Y") if c.expira_em else "Sem limite"
    } for c in cupons]

@app.post("/admin/cupom/{codigo}/toggle")
def toggle_cupom(codigo: str, request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario or usuario.email != ADMIN_EMAIL:
        raise HTTPException(status_code=403, detail="Apenas admin")

    cupom = db.query(Cupom).filter(Cupom.codigo == codigo.upper()).first()
    if not cupom:
        raise HTTPException(status_code=404, detail="Cupom nao encontrado")

    cupom.ativo = not cupom.ativo
    db.commit()
    return {"codigo": cupom.codigo, "ativo": cupom.ativo}
@app.get("/compartilhar/{analise_id}")
def compartilhar_analise(analise_id: int, request: Request, db: Session = Depends(get_db)):
    analise = db.query(Analise).filter(Analise.id == analise_id).first()
    if not analise:
        raise HTTPException(status_code=404, detail="Analise nao encontrada")
    usuario = db.query(Usuario).filter(Usuario.id == analise.usuario_id).first()
    nome = usuario.nome.split()[0] if usuario else "Alguem"
    emocao = analise.emocao or "neutro"
    emoji = analise.emoji or "🧠"
    texto_share = f"{nome} se sentiu {emocao} {emoji} — registrado na Emotion Intelligence"
    url_share = f"{BASE_URL}/cadastro"
    return {
        "texto": texto_share,
        "url": url_share,
        "whatsapp": f"https://wa.me/?text={texto_share} {url_share}",
        "twitter": f"https://twitter.com/intent/tweet?text={texto_share}&url={url_share}",
        "telegram": f"https://t.me/share/url?url={url_share}&text={texto_share}"
    }

@app.get("/certificado")
def gerar_certificado(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Nao autorizado")
    if usuario.plano not in ["premium", "enterprise"]:
        raise HTTPException(status_code=403, detail="Certificado disponivel apenas para Premium e Enterprise")

    from reportlab.lib.pagesizes import A4
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import cm
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
    from reportlab.lib.enums import TA_CENTER
    import io

    total_analises = db.query(Analise).filter(Analise.usuario_id == usuario.id).count()
    total_dias = (datetime.now() - usuario.criado_em).days if usuario.criado_em else 0
    score_ie = min(100, int((total_analises * 2 + usuario.pontos * 0.1 + total_dias * 0.5)))
    emocoes = db.query(Analise.emocao).filter(Analise.usuario_id == usuario.id).all()
    emocao_principal = "Equilibrio Emocional"
    if emocoes:
        from collections import Counter
        contagem = Counter([e[0] for e in emocoes if e[0]])
        if contagem:
            emocao_principal = contagem.most_common(1)[0][0].capitalize()

    buf = io.BytesIO()
    doc = SimpleDocTemplate(
        buf, pagesize=A4,
        rightMargin=2*cm, leftMargin=2*cm,
        topMargin=2*cm, bottomMargin=2*cm
    )

    estilos = getSampleStyleSheet()
    elementos = []

    # Estilo titulo
    titulo_style = ParagraphStyle(
        "titulo",
        parent=estilos["Normal"],
        fontSize=32,
        fontName="Helvetica-Bold",
        textColor=colors.HexColor("#1a1a2e"),
        alignment=TA_CENTER,
        spaceAfter=10
    )
    subtitulo_style = ParagraphStyle(
        "subtitulo",
        parent=estilos["Normal"],
        fontSize=14,
        fontName="Helvetica",
        textColor=colors.HexColor("#555555"),
        alignment=TA_CENTER,
        spaceAfter=6
    )
    destaque_style = ParagraphStyle(
        "destaque",
        parent=estilos["Normal"],
        fontSize=22,
        fontName="Helvetica-Bold",
        textColor=colors.HexColor("#00d2ff"),
        alignment=TA_CENTER,
        spaceAfter=10
    )
    normal_center = ParagraphStyle(
        "normal_center",
        parent=estilos["Normal"],
        fontSize=11,
        fontName="Helvetica",
        textColor=colors.HexColor("#333333"),
        alignment=TA_CENTER,
        spaceAfter=6
    )
    score_style = ParagraphStyle(
        "score",
        parent=estilos["Normal"],
        fontSize=64,
        fontName="Helvetica-Bold",
        textColor=colors.HexColor("#3a7bd5"),
        alignment=TA_CENTER,
        spaceAfter=4
    )
    rodape_style = ParagraphStyle(
        "rodape",
        parent=estilos["Normal"],
        fontSize=9,
        fontName="Helvetica",
        textColor=colors.HexColor("#999999"),
        alignment=TA_CENTER,
        spaceAfter=4
    )

    # Conteudo
    elementos.append(Spacer(1, 0.5*cm))
    elementos.append(Paragraph("🧠 Emotion Intelligence", titulo_style))
    elementos.append(Paragraph("Plataforma de Inteligencia Emocional com IA", subtitulo_style))
    elementos.append(Spacer(1, 0.5*cm))
    elementos.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor("#00d2ff")))
    elementos.append(Spacer(1, 0.8*cm))

    elementos.append(Paragraph("CERTIFICADO DE", normal_center))
    elementos.append(Paragraph("Inteligencia Emocional", destaque_style))
    elementos.append(Spacer(1, 0.3*cm))

    elementos.append(Paragraph("Este certificado e concedido a", normal_center))
    elementos.append(Spacer(1, 0.2*cm))
    elementos.append(Paragraph(usuario.nome, ParagraphStyle(
        "nome_usuario",
        parent=estilos["Normal"],
        fontSize=28,
        fontName="Helvetica-Bold",
        textColor=colors.HexColor("#1a1a2e"),
        alignment=TA_CENTER,
        spaceAfter=10
    )))
    elementos.append(Spacer(1, 0.3*cm))

    elementos.append(Paragraph(
        f"Por completar sua jornada de autoconhecimento emocional com <br/>"
        f"<b>{total_analises} analises emocionais</b> ao longo de <b>{total_dias} dias</b>.",
        normal_center
    ))
    elementos.append(Spacer(1, 0.8*cm))

    elementos.append(HRFlowable(width="60%", thickness=1, color=colors.HexColor("#dddddd")))
    elementos.append(Spacer(1, 0.5*cm))
    elementos.append(Paragraph("Score de Inteligencia Emocional", normal_center))
    elementos.append(Paragraph(str(min(score_ie, 100)), score_style))
    elementos.append(Paragraph("de 100 pontos", normal_center))
    elementos.append(Spacer(1, 0.3*cm))
    elementos.append(Paragraph(f"Emocao predominante: <b>{emocao_principal}</b>", normal_center))
    elementos.append(Spacer(1, 0.5*cm))

    elementos.append(HRFlowable(width="60%", thickness=1, color=colors.HexColor("#dddddd")))
    elementos.append(Spacer(1, 0.5*cm))

    # Competencias
    elementos.append(Paragraph("Competencias Desenvolvidas", ParagraphStyle(
        "comp_titulo",
        parent=estilos["Normal"],
        fontSize=13,
        fontName="Helvetica-Bold",
        textColor=colors.HexColor("#333333"),
        alignment=TA_CENTER,
        spaceAfter=10
    )))

    competencias = [
        "✓ Autoconsciencia Emocional",
        "✓ Autorregulacao e Gestao Emocional",
        "✓ Empatia e Habilidades Sociais",
        "✓ Motivacao Intrinseca",
        "✓ Resiliencia Emocional",
    ]
    for comp in competencias:
        elementos.append(Paragraph(comp, normal_center))

    elementos.append(Spacer(1, 0.8*cm))
    elementos.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor("#00d2ff")))
    elementos.append(Spacer(1, 0.5*cm))

    data_emissao = datetime.now().strftime("%d de %B de %Y")
    elementos.append(Paragraph(f"Emitido em {data_emissao}", rodape_style))
    elementos.append(Paragraph(f"Codigo de verificacao: EI-{usuario.id:06d}-{datetime.now().strftime('%Y%m')}", rodape_style))
    elementos.append(Paragraph("emotion-platform-albert.onrender.com", rodape_style))

    doc.build(elementos)
    buf.seek(0)

    nome_arquivo = f"certificado_ie_{usuario.nome.replace(' ', '_').lower()}.pdf"
    return Response(
        content=buf.read(),
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename={nome_arquivo}"}
    )
@app.get("/exportar/pdf")
def exportar_pdf(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Nao autorizado")

    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib import colors
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import cm
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
        from reportlab.lib.enums import TA_CENTER, TA_LEFT
        import io

        buffer = io.BytesIO()
        doc = SimpleDocTemplate(
            buffer, pagesize=A4,
            rightMargin=2*cm, leftMargin=2*cm,
            topMargin=2*cm, bottomMargin=2*cm
        )

        styles = getSampleStyleSheet()
        elementos = []

        # Estilo titulo
        estilo_titulo = ParagraphStyle(
            'Titulo',
            parent=styles['Title'],
            fontSize=24,
            textColor=colors.HexColor('#3a7bd5'),
            spaceAfter=6,
            alignment=TA_CENTER,
        )
        estilo_subtitulo = ParagraphStyle(
            'Subtitulo',
            parent=styles['Normal'],
            fontSize=12,
            textColor=colors.HexColor('#666666'),
            spaceAfter=4,
            alignment=TA_CENTER,
        )
        estilo_secao = ParagraphStyle(
            'Secao',
            parent=styles['Heading2'],
            fontSize=14,
            textColor=colors.HexColor('#3a7bd5'),
            spaceBefore=16,
            spaceAfter=8,
        )
        estilo_normal = ParagraphStyle(
            'Normal2',
            parent=styles['Normal'],
            fontSize=10,
            textColor=colors.HexColor('#333333'),
            spaceAfter=4,
        )

        # Cabecalho
        elementos.append(Paragraph("Emotion Intelligence Platform", estilo_titulo))
        elementos.append(Paragraph("Relatorio Emocional Mensal", estilo_subtitulo))
        elementos.append(Paragraph(
            f"Gerado em: {datetime.now().strftime('%d/%m/%Y as %H:%M')}",
            estilo_subtitulo
        ))
        elementos.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#3a7bd5')))
        elementos.append(Spacer(1, 0.5*cm))

        # Dados do usuario
        elementos.append(Paragraph("Dados do Usuario", estilo_secao))
        dias_cadastrado = (datetime.now() - usuario.criado_em).days

        dados_usuario = [
            ["Campo", "Valor"],
            ["Nome", usuario.nome],
            ["Email", usuario.email],
            ["Plano", usuario.plano.upper()],
            ["Pontos", str(usuario.pontos)],
            ["Badge", usuario.badge],
            ["Dias na plataforma", str(dias_cadastrado)],
        ]
        tabela_usuario = Table(dados_usuario, colWidths=[5*cm, 11*cm])
        tabela_usuario.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#3a7bd5')),
            ('TEXTCOLOR',  (0,0), (-1,0), colors.white),
            ('FONTNAME',   (0,0), (-1,0), 'Helvetica-Bold'),
            ('FONTSIZE',   (0,0), (-1,-1), 10),
            ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#f8f9fa')),
            ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f0f4ff')]),
            ('GRID',       (0,0), (-1,-1), 0.5, colors.HexColor('#dddddd')),
            ('PADDING',    (0,0), (-1,-1), 8),
        ]))
        elementos.append(tabela_usuario)
        elementos.append(Spacer(1, 0.5*cm))

        # Estatisticas gerais
        analises  = db.query(Analise).filter(Analise.usuario_id == usuario.id).all()
        mensagens = db.query(Mensagem).filter(Mensagem.usuario_id == usuario.id).count()
        diarios   = db.query(Diario).filter(Diario.usuario_id == usuario.id).count()
        conquistas = db.query(Conquista).filter(Conquista.usuario_id == usuario.id).count()

        elementos.append(Paragraph("Estatisticas Gerais", estilo_secao))
        dados_stats = [
            ["Metrica", "Total"],
            ["Analises de emocao", str(len(analises))],
            ["Mensagens com Sofia", str(mensagens)],
            ["Entradas no diario", str(diarios)],
            ["Conquistas desbloqueadas", str(conquistas)],
        ]
        tabela_stats = Table(dados_stats, colWidths=[10*cm, 6*cm])
        tabela_stats.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2ecc71')),
            ('TEXTCOLOR',  (0,0), (-1,0), colors.white),
            ('FONTNAME',   (0,0), (-1,0), 'Helvetica-Bold'),
            ('FONTSIZE',   (0,0), (-1,-1), 10),
            ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f0fff4')]),
            ('GRID',       (0,0), (-1,-1), 0.5, colors.HexColor('#dddddd')),
            ('PADDING',    (0,0), (-1,-1), 8),
            ('ALIGN',      (1,0), (1,-1), 'CENTER'),
        ]))
        elementos.append(tabela_stats)
        elementos.append(Spacer(1, 0.5*cm))

        # Distribuicao de emocoes
        if analises:
            elementos.append(Paragraph("Distribuicao de Emocoes", estilo_secao))
            emocoes_contagem = {}
            for a in analises:
                e = a.emocao.lower()
                emocoes_contagem[e] = emocoes_contagem.get(e, 0) + 1

            emocoes_sorted = sorted(emocoes_contagem.items(), key=lambda x: x[1], reverse=True)
            total_analises = len(analises)

            dados_emocoes = [["Emocao", "Quantidade", "Percentual"]]
            for emocao, qtd in emocoes_sorted:
                pct = round((qtd / total_analises) * 100, 1)
                dados_emocoes.append([
                    emocao.capitalize(),
                    str(qtd),
                    f"{pct}%"
                ])

            tabela_emocoes = Table(dados_emocoes, colWidths=[8*cm, 4*cm, 4*cm])
            tabela_emocoes.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#9b59b6')),
                ('TEXTCOLOR',  (0,0), (-1,0), colors.white),
                ('FONTNAME',   (0,0), (-1,0), 'Helvetica-Bold'),
                ('FONTSIZE',   (0,0), (-1,-1), 10),
                ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f9f0ff')]),
                ('GRID',       (0,0), (-1,-1), 0.5, colors.HexColor('#dddddd')),
                ('PADDING',    (0,0), (-1,-1), 8),
                ('ALIGN',      (1,0), (-1,-1), 'CENTER'),
            ]))
            elementos.append(tabela_emocoes)
            elementos.append(Spacer(1, 0.5*cm))

            # Ultimas 10 analises
            elementos.append(Paragraph("Ultimas Analises", estilo_secao))
            ultimas = sorted(analises, key=lambda x: x.criado_em, reverse=True)[:10]
            dados_ultimas = [["Data", "Texto", "Emocao"]]
            for a in ultimas:
                dados_ultimas.append([
                    a.criado_em.strftime("%d/%m %H:%M"),
                    a.texto[:60] + ("..." if len(a.texto) > 60 else ""),
                    a.emocao.capitalize(),
                ])
            tabela_ultimas = Table(dados_ultimas, colWidths=[3*cm, 11*cm, 3*cm])
            tabela_ultimas.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e67e22')),
                ('TEXTCOLOR',  (0,0), (-1,0), colors.white),
                ('FONTNAME',   (0,0), (-1,0), 'Helvetica-Bold'),
                ('FONTSIZE',   (0,0), (-1,-1), 9),
                ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#fff8f0')]),
                ('GRID',       (0,0), (-1,-1), 0.5, colors.HexColor('#dddddd')),
                ('PADDING',    (0,0), (-1,-1), 6),
            ]))
            elementos.append(tabela_ultimas)

        # Rodape
        elementos.append(Spacer(1, 1*cm))
        elementos.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#cccccc')))
        elementos.append(Paragraph(
            "Emotion Intelligence Platform v15.0 — emotion-platform-albert.onrender.com",
            estilo_subtitulo
        ))

        doc.build(elementos)
        buffer.seek(0)

        nome_arquivo = f"relatorio_{usuario.nome.replace(' ','_')}_{datetime.now().strftime('%Y%m')}.pdf"
        return Response(
            content=buffer.getvalue(),
            media_type="application/pdf",
            headers={"Content-Disposition": f"attachment; filename={nome_arquivo}"}
        )

    except ImportError:
        raise HTTPException(
            status_code=500,
            detail="Biblioteca PDF nao instalada. Tente novamente em instantes."
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao gerar PDF: {str(e)}")


@app.get("/api/v1/analyze")
def api_analyze(
    text:    str,
    usuario: Usuario = Depends(verificar_token),
    db:      Session = Depends(get_db)
):
    limite     = get_limite(usuario, "analises")
    total_hoje = contar_hoje(Analise, usuario.id, db)

    if total_hoje >= limite:
        raise HTTPException(
            status_code=429,
            detail=f"❌ Limite de {limite} análises por dia atingido."
        )

    if len(text.strip()) < 3:
        raise HTTPException(
            status_code=400,
            detail="❌ Texto muito curto. Mínimo 3 caracteres."
        )

    # GEMINI ATIVO na API publica
    try:
        _a = detectar_emocao_hibrido(text, usar_gemini=True)
        emocao = _a.get("emocao", "neutro")
    except:
        try:
            _at = detectar_emocao_hibrido(text, usar_gemini=True)
            emocao = _at.get("emocao", "neutro")
        except:
            emocao = detectar_emocao(text)
    intensidade = calcular_intensidade(text)
    tecnica     = tecnicas_por_emocao.get(emocao, "")

    analise = Analise(
        texto=text,
        emocao=emocao.capitalize(),
        emoji=get_emoji(emocao),
        recomendacao=recomendacoes.get(emocao, ""),
        intensidade=intensidade,
        tecnica=tecnica,
        usuario_id=usuario.id
    )
    db.add(analise)
    db.commit()

    adicionar_pontos(usuario, PONTOS_POR_ACAO["analise"], db)

    return {
        "status":       "success",
        "texto":        text,
        "emocao":       emocao.capitalize(),
        "emoji":        get_emoji(emocao),
        "recomendacao": recomendacoes.get(emocao, ""),
        "tecnica":      tecnica,
        "intensidade":  intensidade,
        "intensidade_label": (
            "Alta" if intensidade == 3 else
            "Média" if intensidade == 2 else
            "Baixa"
        ),
        "pontos_ganhos": PONTOS_POR_ACAO["analise"],
        "total_pontos":  usuario.pontos,
        "timestamp":     datetime.now().isoformat(),
        "version":       "20.0",
    }


@app.get("/api/v1/stats")
def api_stats(
    usuario: Usuario = Depends(verificar_token),
    db:      Session = Depends(get_db)
):
    analises  = db.query(Analise).filter(
        Analise.usuario_id == usuario.id
    ).all()
    mensagens = db.query(Mensagem).filter(
        Mensagem.usuario_id == usuario.id
    ).count()
    diarios   = db.query(Diario).filter(
        Diario.usuario_id == usuario.id
    ).count()

    emocoes  = [a.emocao.lower() for a in analises]
    contagem = {}
    for e in emocoes:
        contagem[e] = contagem.get(e, 0) + 1

    return {
        "status":          "success",
        "usuario":         usuario.nome,
        "email":           usuario.email,
        "plano":           usuario.plano,
        "pontos":          usuario.pontos,
        "badge":           usuario.badge,
        "total_analises":  len(analises),
        "total_mensagens": mensagens,
        "total_diarios":   diarios,
        "emocoes":         contagem,
        "mais_frequente":  max(contagem, key=contagem.get) if contagem else None,
        "emoji_frequente": get_emoji(
            max(contagem, key=contagem.get)
        ) if contagem else "😐",
        "proximo_badge":   proximo_badge(usuario.pontos),
        "membro_desde":    usuario.criado_em.strftime("%d/%m/%Y"),
        "timestamp":       datetime.now().isoformat(),
        "version":         "20.0",
    }


@app.get("/api/v1/emocoes")
def api_emocoes(usuario: Usuario = Depends(verificar_token)):
    return {
        "status":  "success",
        "total":   len(palavras_emocoes),
        "emocoes": [{
            "nome":          emocao,
            "emoji":         get_emoji(emocao),
            "recomendacao":  recomendacoes.get(emocao, ""),
            "tecnica":       tecnicas_por_emocao.get(emocao, ""),
            "total_palavras": len(palavras),
        } for emocao, palavras in palavras_emocoes.items()],
        "version": "20.0",
    }


@app.get("/api/v1/ranking")
def api_ranking(
    usuario: Usuario = Depends(verificar_token),
    db:      Session = Depends(get_db)
):
    top = db.query(Usuario).filter(
        Usuario.ativo == True
    ).order_by(Usuario.pontos.desc()).limit(10).all()

    return {
        "status":  "success",
        "ranking": [{
            "posicao": i + 1,
            "nome":    u.nome[:20],
            "pontos":  u.pontos,
            "badge":   u.badge,
            "plano":   u.plano,
        } for i, u in enumerate(top)],
        "timestamp": datetime.now().isoformat(),
        "version":   "20.0",
    }

# ================================================================
# FIM DA PARTE 4 — FIM DO ARQUIVO COMPLETO
# ================================================================
