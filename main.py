# ================================================================
# EMOTION INTELLIGENCE PLATFORM - v14.0 ULTIMATE
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
Base.metadata.create_all(bind=engine)

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
        "alegria":   "😄",
        "tristeza":  "😢",
        "raiva":     "😡",
        "medo":      "😨",
        "surpresa":  "😲",
        "nojo":      "🤢",
        "amor":      "❤️",
        "esperanca": "🌅",
        "gratidao":  "🙏",
        "solidao":   "😔",
        "euforia":   "🎉",
        "calma":     "🕊️",
        "confusao":  "😕",
        "vergonha":  "😳",
        "neutro":    "😐",
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


def detectar_emocao(texto: str) -> str:
    texto_norm = normalizar_texto(texto)
    pontuacao  = {}

    for emocao, palavras_list in palavras_emocoes.items():
        pontos = 0
        for palavra in palavras_list:
            palavra_norm = normalizar_texto(palavra)
            if palavra_norm in texto_norm:
                # Palavras maiores valem mais
                pontos += len(palavra_norm.split())
        if pontos > 0:
            pontuacao[emocao] = pontos

    if not pontuacao:
        return "neutro"

    return max(pontuacao, key=pontuacao.get)


def calcular_intensidade(texto: str) -> int:
    intensificadores = [
        "muito", "demais", "extremamente", "super", "mega",
        "completamente", "totalmente", "absurdamente", "profundamente",
        "imensamente", "terrivelmente", "incrivelmente", "demasiadamente",
        "excessivamente", "extraordinariamente", "infinitamente"
    ]
    texto_lower = texto.lower()
    tem_intensificador = any(i in texto_lower for i in intensificadores)
    tem_exclamacao     = texto.count('!') >= 2
    tem_maiusculas     = sum(1 for c in texto if c.isupper()) > len(texto) * 0.3
    texto_longo        = len(texto) > 150

    score = sum([
        tem_intensificador,
        tem_exclamacao,
        tem_maiusculas,
        texto_longo
    ])

    if score >= 2:
        return 3
    if score == 1:
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
                    v14.0 ULTIMATE
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

        conteudo = f"""
        <h2 style="color: #333; margin-top: 0;">
            Olá, {usuario.nome}! 📊
        </h2>
        <p style="color: #555; line-height: 1.6;">
            Aqui está seu relatório emocional da semana.
            Você está fazendo um ótimo trabalho ao se conhecer melhor! 🌟
        </p>
        <div style="
            display: grid;
            gap: 15px;
            margin: 20px 0;
        ">
            <div style="
                background: #f0f8ff;
                border-radius: 12px;
                padding: 20px;
                border-left: 4px solid #00d2ff;
            ">
                <h3 style="color: #00d2ff; margin: 0 0 10px;">
                    📈 Resumo da Semana
                </h3>
                <ul style="color: #333; line-height: 2; margin: 0; padding-left: 20px;">
                    <li>Total de análises: <strong>{len(analises)}</strong></li>
                    <li>Entradas no diário: <strong>{diarios_semana}</strong></li>
                    <li>Conversas com Sofia: <strong>{msgs_semana}</strong></li>
                    <li>Intensidade média: <strong>{intensidade_media}/3</strong></li>
                </ul>
            </div>
            <div style="
                background: #fff8f0;
                border-radius: 12px;
                padding: 20px;
                border-left: 4px solid #f39c12;
            ">
                <h3 style="color: #f39c12; margin: 0 0 10px;">
                    🎭 Emoções Detectadas
                </h3>
                <ul style="color: #333; line-height: 1.8; margin: 0; padding-left: 20px;">
                    {lista_html}
                </ul>
                <p style="color: #f39c12; margin: 10px 0 0;">
                    <strong>Emoção mais frequente:</strong>
                    {get_emoji(mais_freq)} {mais_freq.capitalize()}
                </p>
            </div>
            <div style="
                background: #f0fff4;
                border-radius: 12px;
                padding: 20px;
                border-left: 4px solid #2ecc71;
            ">
                <h3 style="color: #2ecc71; margin: 0 0 10px;">
                    🏆 Sua Conquista
                </h3>
                <p style="color: #333; margin: 0;">
                    Pontos totais: <strong>{usuario.pontos}</strong><br>
                    Badge atual: <strong>{usuario.badge}</strong>
                </p>
            </div>
        </div>
        {botao_email("📊 Ver Dashboard Completo", BASE_URL)}
        <p style="
            color: #888;
            font-size: 13px;
            text-align: center;
            margin-top: 20px;
        ">
            Continue assim! Cada análise é um passo em direção
            ao autoconhecimento. 💙
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
    db: Session = SessionLocal()
    try:
        agora = datetime.now()
        usuarios = db.query(Usuario).filter(Usuario.plano == 'free').all()
        import asyncio
        for u in usuarios:
            if not u.criado_em:
                continue
            dias = (agora - u.criado_em).days
            if dias == 1:
                asyncio.run(enviar_email_dia1(u.nome, u.email))
            elif dias == 3:
                asyncio.run(enviar_email_dia3(u.nome, u.email))
            elif dias == 7:
                asyncio.run(enviar_email_dia7(u.nome, u.email))
            elif dias == 14:
                asyncio.run(enviar_email_dia14(u.nome, u.email))
    except Exception as e:
        print(f'[ONBOARDING] Erro: {e}')
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
    version="14.0",
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
            "version":         "14.0 ULTIMATE",
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
            "version": "14.0 ULTIMATE"
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
        return RedirectResponse(url="/login")
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

        prompt_foto = """Analise a expressao facial e linguagem corporal nesta imagem.
Identifique a emocao principal dentre: alegria, tristeza, raiva, medo, surpresa, nojo, ansiedade, calma, confianca, curiosidade, amor, gratidao, frustracao, vergonha, neutro.
Responda EXATAMENTE neste formato JSON:
{
  "emocao": "nome_da_emocao",
  "confianca": 85,
  "descricao": "Descricao curta do que voce observou na imagem",
  "dica": "Uma dica pratica relacionada a esta emocao"
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
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autorizado")

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

    emocao      = detectar_emocao(text)
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
    ).order_by(Mensagem.criado_em.desc()).limit(8).all()

    contexto = ""
    for h in reversed(historico):
        contexto += f"Usuário: {h.conteudo}\nSofia: {h.resposta}\n\n"

    emocao_atual = detectar_emocao(mensagem)
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

    # Historico compacto - ultimas 3 trocas
    historico_curto = ""
    for h in reversed(historico[-3:]):
        historico_curto += f"U: {h.conteudo[:80]}\nS: {h.resposta[:100]}\n"

    prompt = (
        f"Sofia, psicologa virtual brasileira (TCC+Mindfulness). "
        f"Empatica, calorosa, humana. Nunca substitui psicologo real.\n\n"
        f"USUARIO: {usuario.nome} | {usuario.plano.upper()} | "
        f"{usuario.pontos} pts | Badge: {usuario.badge} | "
        f"Emocao: {emocao_atual} {get_emoji(emocao_atual)}\n\n"
        f"INSTRUCOES: {instrucoes_plano}\n\n"
        f"HISTORICO:\n{historico_curto if historico_curto else 'Primeira mensagem.'}\n"
        f"MENSAGEM: {mensagem}\n\n"
        f"Responda como Sofia em portugues brasileiro:"
    )

    try:
        resposta = cliente_ia.models.generate_content(
            model="gemini-1.5-flash-8b",
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
                f"😊 Que lindo, {usuario.nome}! Sua alegria merece ser celebrada! "
                "A gratidão amplifica emoções positivas — escreva 3 coisas que estão te fazendo bem hoje. "
                "Isso ancora essa energia boa dentro de você! "
                "O que mais está contribuindo para essa sensação maravilhosa? 🌟"
            ),
            "tristeza": (
                f"💙 {usuario.nome}, sinto muito que você esteja passando por isso. "
                "A tristeza é válida — ela nos diz que algo importa para nós. "
                "Tente o Acolhimento: coloque a mão no coração, respire fundo 3 vezes "
                "e diga: 'Estou aqui, estou me ouvindo.' "
                "O que você precisaria ouvir agora de alguém que te ama?"
            ),
            "ansiedade": (
                f"🌿 {usuario.nome}, vamos fazer o Grounding 5-4-3-2-1 juntos: "
                "nomeie 5 coisas que você VÊ, 4 que pode TOCAR, 3 que OUVE, "
                "2 que CHEIRA e 1 que SABOREIA. "
                "Isso traz sua mente de volta ao presente agora. "
                "Como está seu corpo físico nesse momento? 💙"
            ),
            "raiva": (
                f"🔥 {usuario.nome}, sua raiva é válida — algo importante foi tocado. "
                "Tente a Respiração 4-7-8: inspire por 4s, segure por 7s, expire por 8s. "
                "Faça 3 vezes. Isso ativa o sistema parassimpático e reduz a intensidade. "
                "O que exatamente mais te incomoda nessa situação?"
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

    emocao         = detectar_emocao(conteudo + " " + titulo)
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
        background_tasks.add_task(
            enviar_email_premium,
            usuario.nome,
            usuario.email,
            "premium"
        )

    nome = usuario.nome if usuario else "usuário"

    return HTMLResponse(f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Pagamento Aprovado — Emotion Intelligence</title>
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
                border: 1px solid rgba(255,255,255,0.1);
                border-radius: 24px;
                padding: 60px 50px;
                text-align: center;
                max-width: 500px;
                width: 90%;
                animation: fadeIn 0.6s ease;
            }}
            @keyframes fadeIn {{
                from {{ opacity: 0; transform: translateY(30px); }}
                to   {{ opacity: 1; transform: translateY(0); }}
            }}
            .icon {{ font-size: 80px; margin-bottom: 20px; }}
            h1 {{
                font-size: 32px;
                margin-bottom: 15px;
                background: linear-gradient(90deg, #00d2ff, #3a7bd5);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }}
            p {{
                color: rgba(255,255,255,0.7);
                font-size: 16px;
                line-height: 1.6;
                margin-bottom: 15px;
            }}
            .bonus {{
                background: linear-gradient(135deg, rgba(0,210,255,0.1), rgba(58,123,213,0.1));
                border: 1px solid rgba(0,210,255,0.3);
                border-radius: 12px;
                padding: 20px;
                margin: 25px 0;
            }}
            .bonus h3 {{
                color: #00d2ff;
                font-size: 20px;
                margin-bottom: 10px;
            }}
            .btn {{
                display: inline-block;
                background: linear-gradient(90deg, #00d2ff, #3a7bd5);
                color: white;
                padding: 15px 40px;
                border-radius: 50px;
                text-decoration: none;
                font-size: 16px;
                font-weight: bold;
                margin-top: 10px;
                transition: transform 0.2s;
            }}
            .btn:hover {{ transform: scale(1.05); }}
        </style>
    </head>
    <body>
        <div class="card">
            <div class="icon">✅</div>
            <h1>Pagamento Aprovado!</h1>
            <p>Parabéns, <strong>{nome}</strong>! 🎉<br>
            Seu plano Premium foi ativado com sucesso!</p>
            <div class="bonus">
                <h3>🎁 Seus benefícios Premium:</h3>
                <p style="text-align:left; color: rgba(255,255,255,0.8);">
                    ✅ Análises emocionais ilimitadas<br>
                    ✅ Chat ilimitado com Sofia<br>
                    ✅ Diário emocional ilimitado<br>
                    ✅ Sessões terapêuticas completas<br>
                    ✅ Relatórios semanais por email<br>
                    ✅ +{PONTOS_POR_ACAO['premium']} pontos de bônus adicionados! 🏆
                </p>
            </div>
            <a href="/" class="btn">🚀 Acessar Dashboard</a>
        </div>
    </body>
    </html>
    """)


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
        49  if p.plano == "premium"    else
        199 if p.plano == "enterprise" else 0
        for p in pagamentos_aprovados
    )

    receita_mensal = sum(
        49  if p.plano == "premium"    else
        199 if p.plano == "enterprise" else 0
        for p in pagamentos_aprovados
        if p.criado_em >= datetime.now() - timedelta(days=30)
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

    emocao      = detectar_emocao(text)
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
        "version":       "14.0",
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
        "version":         "14.0",
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
        "version": "14.0",
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
        "version":   "14.0",
    }

# ================================================================
# FIM DA PARTE 4 — FIM DO ARQUIVO COMPLETO
# ================================================================
