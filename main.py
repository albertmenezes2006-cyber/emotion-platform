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
    Form, BackgroundTasks, Header
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

DATABASE_URL = "sqlite:///./emotion.db"
engine       = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)
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
        modelo = genai.GenerativeModel("gemini-1.5-flash")
        resposta = modelo.generate_content(prompt)
        texto_resposta = resposta.text
    except Exception as e:
        print(f"[Fallback Ativado] Erro: {e}")
        fallbacks = {
            "alegria": "### Que brilho no olhar! ✨
Fico muito feliz em ver você assim. A alegria é contagiante! Que tal usar essa energia para concluir uma meta importante hoje?",
            "tristeza": "### Sinto seu peso hoje... 💙
Acolha sua tristeza, ela faz parte do processo. Estou aqui para te ouvir sem julgamentos. Respire fundo, você é resiliente.",
            "raiva": "### Respire... 🌬️
A raiva nos mostra onde nossos limites foram cruzados. Antes de agir, tente a técnica da respiração 4-7-8 que te ensinei. Vamos conversar sobre o que causou isso?",
            "medo": "### Você não está só. 🤝
O medo é um mestre cauteloso, mas não deixe que ele segure o leme da sua vida. Qual é o menor passo que você pode dar hoje?",
            "neutro": "### Momento de pausa. ⚖️
O estado neutro é excelente para tomarmos decisões lógicas. Como posso te ajudar a planejar sua semana hoje?"
        }
        texto_resposta = fallbacks.get(emocao_atual, "### Estou aqui por você! 💙
O que você está sentindo é legítimo. Conte-me mais sobre o seu dia, quero te entender melhor.")


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
