# ================================================================
# EMOTION INTELLIGENCE PLATFORM - v13.0 ULTIMATE
# ================================================================
# Funcionalidades:
# ✅ Autenticação completa com sessões seguras
# ✅ Análise de emoções avançada
# ✅ IA Psicóloga Sofia (Google Gemini)
# ✅ Diário emocional
# ✅ Gamificação (pontos + badges + ranking)
# ✅ Planos Free/Premium/Enterprise + Trial 7 dias
# ✅ MercadoPago + Webhook automático
# ✅ SendGrid (boas-vindas, premium, relatório semanal)
# ✅ Relatório semanal automático por email
# ✅ Sistema de afiliados com comissão
# ✅ Painel Admin completo (gerenciar usuários, planos, logs)
# ✅ API pública com token
# ✅ Rate limiting por IP
# ✅ Logs de acesso
# ✅ Health check
# ================================================================

from fastapi import FastAPI, HTTPException, Request, Depends, Form, BackgroundTasks, Header
from fastapi.responses import HTMLResponse, RedirectResponse, Response, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.exception_handlers import http_exception_handler
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Text, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from passlib.context import CryptContext
from datetime import datetime, date, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
import unicodedata
import mercadopago
import sendgrid
from sendgrid.helpers.mail import Mail
import google.generativeai as genai
import uuid
import os
import json
import hashlib
import time
from collections import defaultdict

# ================================================================
# CONFIGURAÇÕES GLOBAIS
# ================================================================

MP_ACCESS_TOKEN  = os.environ.get("MP_ACCESS_TOKEN")
ADMIN_EMAIL      = os.environ.get("ADMIN_EMAIL", "albertmenezes2006@gmail.com")
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
BASE_URL         = os.environ.get("BASE_URL", "https://emotion-platform-albert.onrender.com")
GEMINI_API_KEY   = os.environ.get("GEMINI_API_KEY")
API_SECRET       = os.environ.get("API_SECRET", str(uuid.uuid4()))

# Gemini
genai.configure(api_key=GEMINI_API_KEY)
modelo_ia = genai.GenerativeModel("gemini-1.5-flash")

# Limites por plano
LIMITES = {
    "free":       {"analises": 10, "chat": 5,         "diario": 3},
    "trial":      {"analises": 50, "chat": 20,        "diario": 10},
    "premium":    {"analises": 999999, "chat": 999999, "diario": 999999},
    "enterprise": {"analises": 999999, "chat": 999999, "diario": 999999},
}

PRECOS = {
    "premium":    {"valor": 49,  "nome": "Emotion Premium"},
    "enterprise": {"valor": 199, "nome": "Emotion Enterprise"}
}

COMISSAO_PERCENT = 20

# Rate limiting simples
rate_limit_store = defaultdict(list)

# ================================================================
# BANCO DE DADOS
# ================================================================

DATABASE_URL = "sqlite:///./emotion.db"
engine       = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base         = declarative_base()

# ----------------------------------------------------------------
# MODELOS
# ----------------------------------------------------------------

class Usuario(Base):
    __tablename__ = "usuarios"
    id             = Column(Integer, primary_key=True, index=True)
    nome           = Column(String, nullable=False)
    email          = Column(String, unique=True, index=True, nullable=False)
    senha          = Column(String, nullable=False)
    plano          = Column(String, default="free")
    trial_usado    = Column(Boolean, default=False)
    trial_expira   = Column(DateTime, nullable=True)
    ref_code       = Column(String, unique=True, nullable=True)
    indicado_por   = Column(String, nullable=True)
    pontos         = Column(Integer, default=0)
    badge          = Column(String, default="🌱 Iniciante")
    api_token      = Column(String, unique=True, nullable=True)
    ativo          = Column(Boolean, default=True)
    criado_em      = Column(DateTime, default=datetime.now)
    analises       = relationship("Analise",  back_populates="usuario", cascade="all, delete")
    mensagens      = relationship("Mensagem", back_populates="usuario", cascade="all, delete")
    diarios        = relationship("Diario",   back_populates="usuario", cascade="all, delete")
    logs           = relationship("LogAcesso",back_populates="usuario", cascade="all, delete")

class Analise(Base):
    __tablename__ = "analises"
    id           = Column(Integer, primary_key=True, index=True)
    texto        = Column(String,  nullable=False)
    emocao       = Column(String,  nullable=False)
    emoji        = Column(String,  nullable=False)
    recomendacao = Column(String,  nullable=False)
    intensidade  = Column(Integer, default=1)
    criado_em    = Column(DateTime, default=datetime.now)
    usuario_id   = Column(Integer, ForeignKey("usuarios.id"))
    usuario      = relationship("Usuario", back_populates="analises")

class Mensagem(Base):
    __tablename__ = "mensagens"
    id         = Column(Integer, primary_key=True, index=True)
    conteudo   = Column(Text,    nullable=False)
    resposta   = Column(Text,    nullable=False)
    criado_em  = Column(DateTime, default=datetime.now)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    usuario    = relationship("Usuario", back_populates="mensagens")

class Diario(Base):
    __tablename__ = "diarios"
    id         = Column(Integer, primary_key=True, index=True)
    titulo     = Column(String,  nullable=False)
    conteudo   = Column(Text,    nullable=False)
    emocao     = Column(String,  nullable=True)
    emoji      = Column(String,  nullable=True)
    criado_em  = Column(DateTime, default=datetime.now)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    usuario    = relationship("Usuario", back_populates="diarios")

class LogAcesso(Base):
    __tablename__ = "logs_acesso"
    id         = Column(Integer, primary_key=True, index=True)
    rota       = Column(String,  nullable=False)
    metodo     = Column(String,  nullable=False)
    ip         = Column(String,  nullable=True)
    status     = Column(Integer, nullable=True)
    criado_em  = Column(DateTime, default=datetime.now)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=True)
    usuario    = relationship("Usuario", back_populates="logs")

class Pagamento(Base):
    __tablename__ = "pagamentos"
    id           = Column(Integer, primary_key=True, index=True)
    usuario_id   = Column(Integer, ForeignKey("usuarios.id"))
    plano        = Column(String,  nullable=False)
    valor        = Column(Float,   nullable=False)
    status       = Column(String,  default="pendente")
    mp_id        = Column(String,  nullable=True)
    criado_em    = Column(DateTime, default=datetime.now)

Base.metadata.create_all(bind=engine)

# ================================================================
# SEGURANÇA
# ================================================================

pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")

def hash_senha(senha):
    return pwd_context.hash(senha)

def verificar_senha(senha, hash):
    return pwd_context.verify(senha, hash)

def gerar_ref_code(nome: str):
    base   = nome.lower().replace(" ", "")[:6]
    sufixo = str(uuid.uuid4())[:4]
    return f"{base}{sufixo}"

def gerar_api_token(email: str):
    return hashlib.sha256(f"{email}{uuid.uuid4()}".encode()).hexdigest()

def rate_limit(ip: str, limite: int = 30, janela: int = 60) -> bool:
    agora   = time.time()
    acessos = rate_limit_store[ip]
    acessos = [t for t in acessos if agora - t < janela]
    rate_limit_store[ip] = acessos
    if len(acessos) >= limite:
        return False
    rate_limit_store[ip].append(agora)
    return True

# ================================================================
# APP
# ================================================================

app       = FastAPI(title="Emotion Intelligence Platform", version="13.0")
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
sessoes   = {}

# ================================================================
# MIDDLEWARE DE LOG
# ================================================================

class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        inicio   = time.time()
        response = await call_next(request)
        duracao  = round((time.time() - inicio) * 1000, 2)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {request.method} {request.url.path} → {response.status_code} ({duracao}ms)")
        return response

app.add_middleware(LogMiddleware)

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
    return usuario

def get_limite(usuario, tipo: str) -> int:
    plano = usuario.plano if usuario.plano in LIMITES else "free"
    return LIMITES[plano][tipo]

def contar_hoje(model, usuario_id: int, db: Session):
    hoje = date.today()
    return db.query(model).filter(
        model.usuario_id == usuario_id,
        model.criado_em >= datetime.combine(hoje, datetime.min.time())
    ).count()

def contar_total_usuarios(db: Session):
    return db.query(Usuario).count()

def calcular_badge(pontos: int) -> str:
    if pontos >= 5000: return "👑 Lenda Emocional"
    if pontos >= 2000: return "💎 Mestre Emocional"
    if pontos >= 1000: return "🏆 Especialista"
    if pontos >= 500:  return "⭐ Avançado"
    if pontos >= 200:  return "🔥 Intermediário"
    if pontos >= 50:   return "🌿 Explorador"
    return "🌱 Iniciante"

def adicionar_pontos(usuario, pontos: int, db: Session):
    usuario.pontos += pontos
    usuario.badge   = calcular_badge(usuario.pontos)
    db.commit()

def registrar_log(rota: str, metodo: str, ip: str, status: int,
                  usuario_id: int = None, db: Session = None):
    if db:
        log = LogAcesso(
            rota=rota, metodo=metodo, ip=ip,
            status=status, usuario_id=usuario_id
        )
        db.add(log)
        db.commit()

# ================================================================
# EMAILS
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
    except Exception as e:
        print(f"Erro email: {e}")

async def enviar_email_boas_vindas(nome: str, email: str, ref_code: str):
    link_afiliado = f"{BASE_URL}/?ref={ref_code}"
    enviar_email(email, "🧠 Bem-vindo ao Emotion Intelligence!", f"""
    <html><body style="font-family:sans-serif;padding:40px;background:#f9f9f9">
    <div style="max-width:600px;margin:0 auto;background:#fff;border-radius:20px;padding:40px">
    <h1 style="color:#00d2ff">🧠 Emotion Intelligence</h1>
    <h2>Olá, {nome}! 👋</h2>
    <p>Seja bem-vindo! Com o plano <strong>FREE</strong> você tem:</p>
    <ul>
      <li>✅ 10 análises emocionais por dia</li>
      <li>✅ 5 conversas com a Sofia (IA Psicóloga) por dia</li>
      <li>✅ 3 entradas no diário emocional por dia</li>
      <li>✅ Sistema de pontos e badges</li>
    </ul>
    <br>
    <p><strong>💰 Seu link de afiliado:</strong></p>
    <p style="background:#f0f0f0;padding:10px;border-radius:8px">{link_afiliado}</p>
    <p>Compartilhe e ganhe <strong>20% de comissão</strong> em cada venda!</p>
    <br>
    <a href="{BASE_URL}" style="background:linear-gradient(90deg,#00d2ff,#3a7bd5);
    padding:15px 30px;border-radius:15px;color:#fff;text-decoration:none">
    Acessar Dashboard 🚀</a>
    </div></body></html>""")

async def enviar_email_novo_cadastro(nome: str, email: str):
    enviar_email(ADMIN_EMAIL, f"🎉 Novo cadastro: {nome}", f"""
    <html><body style="font-family:sans-serif;padding:40px">
    <h1 style="color:#00d2ff">🎉 Novo usuário cadastrado!</h1>
    <p><strong>Nome:</strong> {nome}</p>
    <p><strong>Email:</strong> {email}</p>
    <p><strong>Data:</strong> {datetime.now().strftime("%d/%m/%Y %H:%M")}</p>
    <br>
    <a href="{BASE_URL}/admin" style="background:#00d2ff;padding:15px 30px;
    border-radius:15px;color:#fff;text-decoration:none">Ver Painel Admin</a>
    </body></html>""")

async def enviar_email_premium(nome: str, email: str, plano: str = "premium"):
    valor = "R$49/mês" if plano == "premium" else "R$199/mês"
    enviar_email(email, "⭐ Seu plano foi ativado!", f"""
    <html><body style="font-family:sans-serif;padding:40px;background:#f9f9f9">
    <div style="max-width:600px;margin:0 auto;background:#fff;border-radius:20px;padding:40px">
    <h1 style="color:#00d2ff">🧠 Emotion Intelligence</h1>
    <h2>Parabéns, {nome}! 🎉</h2>
    <p>Plano <strong>{plano.capitalize()}</strong> ativado com sucesso!</p>
    <ul>
      <li>✅ Análises ilimitadas</li>
      <li>✅ Chat ilimitado com Sofia</li>
      <li>✅ Diário emocional ilimitado</li>
      <li>✅ Relatórios semanais por email</li>
      <li>✅ Prioridade no suporte</li>
    </ul>
    <br>
    <a href="{BASE_URL}" style="background:linear-gradient(90deg,#00d2ff,#3a7bd5);
    padding:15px 30px;border-radius:15px;color:#fff;text-decoration:none">
    Acessar Dashboard 🚀</a>
    </div></body></html>""")
    enviar_email(ADMIN_EMAIL, f"💰 Novo {plano.capitalize()}: {nome}!", f"""
    <html><body style="font-family:sans-serif;padding:40px">
    <h1 style="color:#2ecc71">💰 Nova assinatura {plano.capitalize()}!</h1>
    <p><strong>Nome:</strong> {nome}</p>
    <p><strong>Email:</strong> {email}</p>
    <p><strong>Valor:</strong> {valor}</p>
    <p><strong>Data:</strong> {datetime.now().strftime("%d/%m/%Y %H:%M")}</p>
    <a href="{BASE_URL}/admin" style="background:#2ecc71;padding:15px 30px;
    border-radius:15px;color:#fff;text-decoration:none">Ver Painel Admin</a>
    </body></html>""")

async def enviar_relatorio_semanal(usuario, db: Session):
    try:
        hoje       = date.today()
        semana     = datetime.now() - timedelta(days=7)
        analises   = db.query(Analise).filter(
            Analise.usuario_id == usuario.id,
            Analise.criado_em  >= semana
        ).all()
        if not analises:
            return
        emocoes  = [a.emocao.lower() for a in analises]
        contagem = {}
        for e in emocoes:
            contagem[e] = contagem.get(e, 0) + 1
        mais_freq   = max(contagem, key=contagem.get)
        lista_html  = "".join([f"<li>{e.capitalize()}: {c}x</li>"
                               for e, c in contagem.items()])
        enviar_email(usuario.email, "📊 Seu relatório emocional semanal!", f"""
        <html><body style="font-family:sans-serif;padding:40px;background:#f9f9f9">
        <div style="max-width:600px;margin:0 auto;background:#fff;border-radius:20px;padding:40px">
        <h1 style="color:#00d2ff">🧠 Relatório Semanal</h1>
        <h2>Olá, {usuario.nome}! 📊</h2>
        <p>Aqui está seu resumo emocional da semana:</p>
        <ul>{lista_html}</ul>
        <p><strong>Emoção mais frequente:</strong> {mais_freq.capitalize()}</p>
        <p><strong>Total de análises:</strong> {len(analises)}</p>
        <p><strong>Seus pontos:</strong> {usuario.pontos} 🏆</p>
        <p><strong>Seu badge:</strong> {usuario.badge}</p>
        <br>
        <a href="{BASE_URL}" style="background:linear-gradient(90deg,#00d2ff,#3a7bd5);
        padding:15px 30px;border-radius:15px;color:#fff;text-decoration:none">
        Ver Dashboard 🚀</a>
        </div></body></html>""")
    except Exception as e:
        print(f"Erro relatório semanal: {e}")

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
            asyncio.run(enviar_relatorio_semanal(u, db))
        print(f"[Scheduler] Relatórios enviados: {len(usuarios)}")
    finally:
        db.close()

scheduler = BackgroundScheduler()
scheduler.add_job(job_relatorio_semanal, "cron", day_of_week="sun", hour=8, minute=0)
scheduler.start()

# ================================================================
# DETECÇÃO DE EMOÇÕES
# ================================================================

palavras_emocoes = {
    "alegria":   ["feliz","alegre","contente","animado","otimo","maravilhoso",
                  "incrivel","satisfeito","radiante","euforico","empolgado",
                  "bem","prazer","alegra","jubilo","vencedor","felicidade",
                  "sorrindo","rindo","divertido","animada","ótimo"],
    "tristeza":  ["triste","deprimido","chateado","desanimado","sozinho",
                  "melancolico","chorando","sofrendo","perdido","abandonado",
                  "luto","dor","pena","lamento","chorar","vazio","angustia",
                  "desesperado","inconsolavel"],
    "raiva":     ["raiva","irritado","furioso","bravo","odio","revoltado",
                  "indignado","nervoso","estressado","explosivo","agressivo",
                  "enfurecido","colera","raivoso","irritada","com raiva"],
    "medo":      ["medo","assustado","apavorado","ansioso","preocupado",
                  "tenso","inseguro","receoso","aterrorizado","ansiedade",
                  "panico","fobia","tremendo","com medo","apavorada"],
    "surpresa":  ["surpreso","chocado","impressionado","espantado","uau",
                  "nossa","caramba","inacreditavel","que","nao acredito"],
    "nojo":      ["nojo","repulsa","asco","horrivel","terrivel","repugnante",
                  "enjoado","asqueroso","que nojo"],
    "amor":      ["amo","amar","amor","carinho","apaixonado","ternura",
                  "beijo","afetuoso","estima","quero","adoro","apaixonada",
                  "saudade","afeto"],
    "esperanca": ["esperanca","esperancoso","otimista","acredito","confiante",
                  "positivo","vai melhorar","tudo vai dar certo","fe"],
    "gratidao":  ["grato","agradecido","obrigado","gratidao","reconhecido",
                  "valorizando","agradecida","muito obrigado"],
    "solidao":   ["sozinho","isolado","abandonado","ninguem","excluido",
                  "sem amigos","me sinto so","nao tenho ninguem"],
    "euforia":   ["euforico","empolgado","animadissimo","fantastico",
                  "extraordinario","incrivel","demais","top","perfeito"],
    "calma":     ["calmo","tranquilo","paz","sereno","relaxado","bem",
                  "equilibrado","centrado","sossegado"],
    "confusao":  ["confuso","perdido","nao sei","incerto","duvida",
                  "indeciso","nao entendo","nao consigo"],
    "vergonha":  ["vergonha","envergonhado","constrangido","humilhado",
                  "timido","acanhado"],
}

recomendacoes = {
    "alegria":   "Continue assim! Compartilhe sua energia positiva! 🌟",
    "tristeza":  "Considere conversar com alguém de confiança. Você não está sozinho. 💙",
    "raiva":     "Respire fundo 4x. Uma pausa pode transformar tudo. 🌬️",
    "medo":      "Identifique a causa. Nomeie o medo — isso já reduz sua intensidade. 🤝",
    "surpresa":  "Absorva o momento! Surpresas fazem parte da jornada. ✨",
    "nojo":      "Afaste-se do que causa desconforto. Cuide do seu espaço. 🛡️",
    "amor":      "O amor enriquece a vida. Valorize e expresse seus sentimentos. ❤️",
    "esperanca": "Continue acreditando! O futuro reserva coisas boas. 🌅",
    "gratidao":  "A gratidão transforma perspectivas. Continue cultivando isso! 🙏",
    "solidao":   "Você não está sozinho. Busque conexões significativas. 🤗",
    "euforia":   "Aproveite esse momento incrível com responsabilidade! 🎉",
    "calma":     "Que momento precioso. Aproveite e recarregue suas energias. 🕊️",
    "confusao":  "Tudo bem não saber. Respire e dê um passo de cada vez. 🧭",
    "vergonha":  "Seja gentil consigo mesmo. Todo mundo erra — é humano. 💚",
    "neutro":    "Momento de equilíbrio. Aproveite a calma! ⚖️"
}

def get_emoji(emocao):
    emojis = {
        "alegria":"😄","tristeza":"😢","raiva":"😡","medo":"😨",
        "surpresa":"😲","nojo":"🤢","amor":"❤️","esperanca":"🌅",
        "gratidao":"🙏","solidao":"😔","euforia":"🎉","calma":"🕊️",
        "confusao":"😕","vergonha":"😳","neutro":"😐"
    }
    return emojis.get(emocao, "😐")

def detectar_emocao(text):
    text_lower      = text.lower()
    text_sem_acento = ''.join(
        c for c in unicodedata.normalize('NFD', text_lower)
        if unicodedata.category(c) != 'Mn'
    )
    pontuacao = {}
    for emocao, palavras_list in palavras_emocoes.items():
        pontos = sum(1 for p in palavras_list if p in text_sem_acento)
        if pontos > 0:
            pontuacao[emocao] = pontos
    return max(pontuacao, key=pontuacao.get) if pontuacao else "neutro"

def calcular_intensidade(text: str) -> int:
    intensificadores = ["muito","demais","extremamente","super","mega",
                        "completamente","totalmente","absurdamente"]
    texto_lower = text.lower()
    for i in intensificadores:
        if i in texto_lower:
            return 3
    if len(text) > 100:
        return 2
    return 1

# ================================================================
# ROTAS — SISTEMA
# ================================================================

@app.get("/health")
async def health():
    db = SessionLocal()
    try:
        total = db.query(Usuario).count()
        return {
            "status":   "healthy",
            "version":  "13.0",
            "usuarios": total,
            "timestamp":datetime.now().isoformat()
        }
    finally:
        db.close()

@app.head("/")
async def head_root():
    return Response(status_code=200)

@app.exception_handler(StarletteHTTPException)
async def custom_404(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return templates.TemplateResponse(request, "404.html", status_code=404)
    return await http_exception_handler(request, exc)

# ================================================================
# ROTAS — PÁGINAS PRINCIPAIS
# ================================================================

@app.get("/", response_class=HTMLResponse)
def index(request: Request, ref: str = None, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        total_usuarios = contar_total_usuarios(db)
        response = templates.TemplateResponse(request, "index.html", {
            "total_usuarios": total_usuarios
        })
        if ref:
            response.set_cookie(key="ref", value=ref, max_age=86400)
        return response
    analises_hoje  = contar_hoje(Analise,   usuario.id, db)
    mensagens_hoje = contar_hoje(Mensagem,  usuario.id, db)
    diarios_hoje   = contar_hoje(Diario,    usuario.id, db)
    ranking        = db.query(Usuario).filter(
        Usuario.ativo == True
    ).order_by(Usuario.pontos.desc()).limit(10).all()
    return templates.TemplateResponse(request, "dashboard.html", {
        "usuario":           usuario,
        "analises_hoje":     analises_hoje,
        "mensagens_hoje":    mensagens_hoje,
        "diarios_hoje":      diarios_hoje,
        "limite_analises":   get_limite(usuario, "analises"),
        "limite_chat":       get_limite(usuario, "chat"),
        "limite_diario":     get_limite(usuario, "diario"),
        "ranking":           ranking,
    })

@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(request, "login.html")

@app.post("/login")
def login(request: Request, email: str = Form(...),
          senha: str = Form(...), db: Session = Depends(get_db)):
    ip      = request.client.host if request.client else "unknown"
    if not rate_limit(ip, limite=10, janela=60):
        return templates.TemplateResponse(request, "login.html", {
            "erro": "Muitas tentativas. Aguarde 1 minuto."
        })
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if not usuario or not verificar_senha(senha, usuario.senha):
        registrar_log("/login", "POST", ip, 401, db=db)
        return templates.TemplateResponse(request, "login.html", {
            "erro": "Email ou senha incorretos"
        })
    if not usuario.ativo:
        return templates.TemplateResponse(request, "login.html", {
            "erro": "Conta desativada. Entre em contato com o suporte."
        })
    session_id          = str(uuid.uuid4())
    sessoes[session_id] = usuario.id
    registrar_log("/login", "POST", ip, 200, usuario.id, db)
    response = RedirectResponse(url="/", status_code=302)
    response.set_cookie(key="session_id", value=session_id, httponly=True)
    return response

@app.get("/cadastro", response_class=HTMLResponse)
def cadastro_page(request: Request):
    return templates.TemplateResponse(request, "cadastro.html")

@app.post("/cadastro")
async def cadastro(background_tasks: BackgroundTasks, request: Request,
                   nome: str  = Form(...), email: str = Form(...),
                   senha: str = Form(...), db: Session = Depends(get_db)):
    ip = request.client.host if request.client else "unknown"
    if not rate_limit(ip, limite=5, janela=300):
        return templates.TemplateResponse(request, "cadastro.html", {
            "erro": "Muitos cadastros. Aguarde 5 minutos."
        })
    existe = db.query(Usuario).filter(Usuario.email == email).first()
    if existe:
        return templates.TemplateResponse(request, "cadastro.html", {
            "erro": "Email já cadastrado"
        })
    ref_cookie  = request.cookies.get("ref")
    ref_code    = gerar_ref_code(nome)
    api_token   = gerar_api_token(email)
    novo = Usuario(
        nome=nome, email=email, senha=hash_senha(senha),
        plano="free", ref_code=ref_code,
        indicado_por=ref_cookie, api_token=api_token
    )
    db.add(novo)
    db.commit()
    adicionar_pontos(novo, 10, db)
    background_tasks.add_task(enviar_email_boas_vindas, nome, email, ref_code)
    background_tasks.add_task(enviar_email_novo_cadastro, nome, email)
    session_id          = str(uuid.uuid4())
    sessoes[session_id] = novo.id
    response = RedirectResponse(url="/obrigado", status_code=302)
    response.set_cookie(key="session_id", value=session_id, httponly=True)
    return response

@app.get("/obrigado", response_class=HTMLResponse)
def obrigado(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return RedirectResponse(url="/login")
    link_afiliado = f"{BASE_URL}/?ref={usuario.ref_code}"
    return templates.TemplateResponse(request, "obrigado.html", {
        "usuario":       usuario,
        "link_afiliado": link_afiliado
    })

@app.get("/logout")
def logout(request: Request):
    session_id = request.cookies.get("session_id")
    if session_id in sessoes:
        del sessoes[session_id]
    response = RedirectResponse(url="/login")
    response.delete_cookie("session_id")
    return response

@app.get("/privacidade", response_class=HTMLResponse)
def privacidade(request: Request):
    return templates.TemplateResponse(request, "privacidade.html")

@app.get("/termos", response_class=HTMLResponse)
def termos(request: Request):
    return templates.TemplateResponse(request, "termos.html")

@app.get("/faq", response_class=HTMLResponse)
def faq(request: Request):
    return templates.TemplateResponse(request, "faq.html")

@app.get("/contato", response_class=HTMLResponse)
def contato(request: Request):
    return templates.TemplateResponse(request, "contato.html")

@app.get("/sobre", response_class=HTMLResponse)
def sobre(request: Request):
    return templates.TemplateResponse(request, "sobre.html")

# ================================================================
# ROTAS — PERFIL
# ================================================================

@app.get("/perfil", response_class=HTMLResponse)
def perfil_page(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return RedirectResponse(url="/login")
    total_analises  = db.query(Analise).filter(Analise.usuario_id == usuario.id).count()
    total_mensagens = db.query(Mensagem).filter(Mensagem.usuario_id == usuario.id).count()
    total_diarios   = db.query(Diario).filter(Diario.usuario_id == usuario.id).count()
    analises_hoje   = contar_hoje(Analise, usuario.id, db)
    dias_cadastrado = (datetime.now() - usuario.criado_em).days
    proximo_badge   = _proximo_badge(usuario.pontos)
    return templates.TemplateResponse(request, "perfil.html", {
        "usuario":        usuario,
        "total_analises": total_analises,
        "total_mensagens":total_mensagens,
        "total_diarios":  total_diarios,
        "analises_hoje":  analises_hoje,
        "dias_cadastrado":dias_cadastrado,
        "proximo_badge":  proximo_badge,
        "api_token":      usuario.api_token
    })

def _proximo_badge(pontos: int):
    niveis = [
        (50,   "🌿 Explorador"),
        (200,  "🔥 Intermediário"),
        (500,  "⭐ Avançado"),
        (1000, "🏆 Especialista"),
        (2000, "💎 Mestre Emocional"),
        (5000, "👑 Lenda Emocional"),
    ]
    for limite, badge in niveis:
        if pontos < limite:
            return {"badge": badge, "faltam": limite - pontos}
    return {"badge": "👑 Máximo atingido!", "faltam": 0}

@app.post("/perfil")
def perfil_update(request: Request, nome: str = Form(...),
                  senha: str = Form(""), confirmar_senha: str = Form(""),
                  db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return RedirectResponse(url="/login")
    total_analises  = db.query(Analise).filter(Analise.usuario_id == usuario.id).count()
    analises_hoje   = contar_hoje(Analise, usuario.id, db)
    dias_cadastrado = (datetime.now() - usuario.criado_em).days
    if senha and senha != confirmar_senha:
        return templates.TemplateResponse(request, "perfil.html", {
            "usuario":usuario,"total_analises":total_analises,
            "analises_hoje":analises_hoje,"dias_cadastrado":dias_cadastrado,
            "erro":"As senhas não coincidem!"
        })
    usuario.nome = nome
    if senha:
        usuario.senha = hash_senha(senha)
    db.commit()
    return templates.TemplateResponse(request, "perfil.html", {
        "usuario":usuario,"total_analises":total_analises,
        "analises_hoje":analises_hoje,"dias_cadastrado":dias_cadastrado,
        "sucesso":"Perfil atualizado com sucesso!"
    })

# ================================================================
# ROTAS — AFILIADOS
# ================================================================

@app.get("/afiliado", response_class=HTMLResponse)
def afiliado_page(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return RedirectResponse(url="/login")
    indicados         = db.query(Usuario).filter(
        Usuario.indicado_por == usuario.ref_code
    ).all()
    indicados_premium = [u for u in indicados if u.plano in ["premium","enterprise"]]
    comissao          = sum(
        49 if u.plano == "premium" else 199
        for u in indicados_premium
    ) * COMISSAO_PERCENT // 100
    return templates.TemplateResponse(request, "afiliado.html", {
        "usuario":          usuario,
        "total_indicados":  len(indicados),
        "indicados_premium":len(indicados_premium),
        "indicados":        indicados,
        "comissao":         comissao,
        "link":             f"{BASE_URL}/?ref={usuario.ref_code}"
    })

# ================================================================
# ROTAS — ANÁLISE DE EMOÇÕES
# ================================================================

@app.get("/analyze")
def analyze(request: Request, text: str, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autorizado")
    limite = get_limite(usuario, "analises")
    if contar_hoje(Analise, usuario.id, db) >= limite:
        raise HTTPException(status_code=429,
            detail=f"Limite de {limite} análises por dia atingido! Faça upgrade. 💎")
    emocao      = detectar_emocao(text)
    intensidade = calcular_intensidade(text)
    analise = Analise(
        texto=text,
        emocao=emocao.capitalize(),
        emoji=get_emoji(emocao),
        recomendacao=recomendacoes.get(emocao, ""),
        intensidade=intensidade,
        usuario_id=usuario.id
    )
    db.add(analise)
    db.commit()
    adicionar_pontos(usuario, 5, db)
    return {
        "texto":        text,
        "emocao":       emocao.capitalize(),
        "emoji":        get_emoji(emocao),
        "recomendacao": recomendacoes.get(emocao, ""),
        "intensidade":  intensidade,
        "pontos_ganhos":5,
        "total_pontos": usuario.pontos,
        "badge":        usuario.badge,
        "timestamp":    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

@app.get("/historico")
def ver_historico(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autorizado")
    analises = db.query(Analise).filter(
        Analise.usuario_id == usuario.id
    ).order_by(Analise.criado_em.desc()).all()
    return {
        "total": len(analises),
        "analises": [{
            "texto":        a.texto,
            "emocao":       a.emocao,
            "emoji":        a.emoji,
            "recomendacao": a.recomendacao,
            "intensidade":  a.intensidade,
            "timestamp":    a.criado_em.strftime("%Y-%m-%d %H:%M:%S")
        } for a in analises]
    }

@app.get("/stats")
def stats(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autorizado")
    analises = db.query(Analise).filter(Analise.usuario_id == usuario.id).all()
    if not analises:
        return {"mensagem": "Nenhuma análise ainda"}
    emocoes  = [a.emocao.lower() for a in analises]
    contagem = {}
    for e in emocoes:
        contagem[e] = contagem.get(e, 0) + 1
    por_dia = {}
    for a in analises:
        dia = a.criado_em.strftime("%d/%m")
        por_dia[dia] = por_dia.get(dia, 0) + 1
    return {
        "total_analises":    len(analises),
        "emocoes_detectadas":contagem,
        "mais_frequente":    max(contagem, key=contagem.get),
        "por_dia":           por_dia,
        "pontos":            usuario.pontos,
        "badge":             usuario.badge
    }

# ================================================================
# ROTAS — IA PSICÓLOGA SOFIA 🧠
# ================================================================

@app.post("/chat")
async def chat(request: Request, mensagem: str = Form(...),
               db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autorizado")
    limite = get_limite(usuario, "chat")
    if contar_hoje(Mensagem, usuario.id, db) >= limite:
        raise HTTPException(status_code=429,
            detail=f"Limite de {limite} mensagens por dia! Faça upgrade para Premium. 💎")
    historico = db.query(Mensagem).filter(
        Mensagem.usuario_id == usuario.id
    ).order_by(Mensagem.criado_em.desc()).limit(8).all()
    contexto = ""
    for h in reversed(historico):
        contexto += f"Usuário: {h.conteudo}\nSofia: {h.resposta}\n\n"
    emocao_atual = detectar_emocao(mensagem)
    prompt = f"""Você é Sofia, psicóloga virtual da plataforma Emotion Intelligence.

Perfil da Sofia:
- Empática, acolhedora, profissional e genuinamente humana
- Usa linguagem simples, calorosa e brasileira
- Faz perguntas abertas para entender melhor o usuário
- Oferece técnicas práticas: respiração 4-7-8, mindfulness, TCC, journaling, EMDR leve
- Reconhece padrões emocionais do histórico da conversa
- Nunca substitui psicólogo real — quando grave, sugere ajuda profissional
- Responde SEMPRE em português brasileiro
- Respostas entre 3 a 7 linhas, diretas e calorosas
- Celebra conquistas do usuário (pontos, badges)
- Conhece o plano do usuário e menciona benefícios quando relevante

Dados do usuário:
- Nome: {usuario.nome}
- Plano: {usuario.plano}
- Pontos: {usuario.pontos}
- Badge: {usuario.badge}
- Emoção detectada agora: {emocao_atual}

Histórico recente:
{contexto if contexto else "Primeira conversa com este usuário."}

Nova mensagem: {mensagem}

Responda como Sofia, com empatia e profissionalismo:"""

    try:
        resposta       = modelo_ia.generate_content(prompt)
        texto_resposta = resposta.text
    except Exception as e:
        texto_resposta = "Desculpe, estou com uma dificuldade técnica agora. Tente novamente em instantes. 💙"
        print(f"Erro Gemini: {e}")

    nova_msg = Mensagem(
        conteudo=mensagem,
        resposta=texto_resposta,
        usuario_id=usuario.id
    )
    db.add(nova_msg)
    db.commit()
    adicionar_pontos(usuario, 2, db)
    return {
        "resposta":        texto_resposta,
        "emocao_detectada":emocao_atual,
        "emoji":           get_emoji(emocao_atual),
        "mensagens_hoje":  contar_hoje(Mensagem, usuario.id, db),
        "limite_chat":     limite,
        "pontos_ganhos":   2,
        "total_pontos":    usuario.pontos,
        "badge":           usuario.badge,
        "plano":           usuario.plano
    }

@app.get("/chat/historico")
def historico_chat(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autorizado")
    mensagens = db.query(Mensagem).filter(
        Mensagem.usuario_id == usuario.id
    ).order_by(Mensagem.criado_em.asc()).all()
    return {
        "total": len(mensagens),
        "mensagens": [{
            "conteudo":  m.conteudo,
            "resposta":  m.resposta,
            "timestamp": m.criado_em.strftime("%d/%m/%Y %H:%M")
        } for m in mensagens]
    }

# ================================================================
# ROTAS — DIÁRIO EMOCIONAL
# ================================================================

@app.post("/diario")
def criar_diario(request: Request, titulo: str = Form(...),
                 conteudo: str = Form(...), db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autorizado")
    limite = get_limite(usuario, "diario")
    if contar_hoje(Diario, usuario.id, db) >= limite:
        raise HTTPException(status_code=429,
            detail=f"Limite de {limite} entradas por dia! Faça upgrade. 💎")
    emocao = detectar_emocao(conteudo)
    novo   = Diario(
        titulo=titulo, conteudo=conteudo,
        emocao=emocao.capitalize(),
        emoji=get_emoji(emocao),
        usuario_id=usuario.id
    )
    db.add(novo)
    db.commit()
    adicionar_pontos(usuario, 8, db)
    return {
        "mensagem":     "Entrada salva com sucesso!",
        "emocao":       emocao.capitalize(),
        "emoji":        get_emoji(emocao),
        "pontos_ganhos":8,
        "total_pontos": usuario.pontos,
        "badge":        usuario.badge
    }

@app.get("/diario")
def ver_diario(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autorizado")
    entradas = db.query(Diario).filter(
        Diario.usuario_id == usuario.id
    ).order_by(Diario.criado_em.desc()).all()
    return {
        "total": len(entradas),
        "entradas": [{
            "id":        e.id,
            "titulo":    e.titulo,
            "conteudo":  e.conteudo,
            "emocao":    e.emocao,
            "emoji":     e.emoji,
            "timestamp": e.criado_em.strftime("%d/%m/%Y %H:%M")
        } for e in entradas]
    }

@app.delete("/diario/{diario_id}")
def deletar_diario(diario_id: int, request: Request,
                   db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autorizado")
    entrada = db.query(Diario).filter(
        Diario.id == diario_id,
        Diario.usuario_id == usuario.id
    ).first()
    if not entrada:
        raise HTTPException(status_code=404, detail="Entrada não encontrada")
    db.delete(entrada)
    db.commit()
    return {"mensagem": "Entrada deletada com sucesso!"}

# ================================================================
# ROTAS — GAMIFICAÇÃO
# ================================================================

@app.get("/ranking")
def ranking(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autorizado")
    top = db.query(Usuario).filter(
        Usuario.ativo == True
    ).order_by(Usuario.pontos.desc()).limit(20).all()
    posicao = next(
        (i+1 for i, u in enumerate(top) if u.id == usuario.id), None
    )
    return {
        "minha_posicao": posicao,
        "meus_pontos":   usuario.pontos,
        "meu_badge":     usuario.badge,
        "ranking": [{
            "posicao": i+1,
            "nome":    u.nome[:20],
            "pontos":  u.pontos,
            "badge":   u.badge,
            "plano":   u.plano
        } for i, u in enumerate(top)]
    }

# ================================================================
# ROTAS — TRIAL
# ================================================================

@app.post("/trial")
def ativar_trial(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autorizado")
    if usuario.trial_usado:
        raise HTTPException(status_code=400,
            detail="Trial já utilizado. Faça upgrade para Premium. 💎")
    if usuario.plano != "free":
        raise HTTPException(status_code=400,
            detail="Você já tem um plano ativo.")
    usuario.plano        = "trial"
    usuario.trial_usado  = True
    usuario.trial_expira = datetime.now() + timedelta(days=7)
    db.commit()
    adicionar_pontos(usuario, 20, db)
    return {
        "mensagem":    "Trial Premium ativado por 7 dias! 🎉",
        "expira_em":   usuario.trial_expira.strftime("%d/%m/%Y"),
        "pontos_ganhos":20
    }

# ================================================================
# ROTAS — PLANOS E PAGAMENTO
# ================================================================

@app.get("/planos", response_class=HTMLResponse)
def planos(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return RedirectResponse(url="/login")
    return templates.TemplateResponse(request, "planos.html", {
        "usuario": usuario
    })

@app.get("/checkout")
def checkout(request: Request, plano: str, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return RedirectResponse(url="/login")
    if plano not in PRECOS:
        raise HTTPException(status_code=400, detail="Plano inválido")
    try:
        sdk = mercadopago.SDK(MP_ACCESS_TOKEN)
        preference_data = {
            "items": [{
                "title":       PRECOS[plano]["nome"],
                "quantity":    1,
                "currency_id": "BRL",
                "unit_price":  float(PRECOS[plano]["valor"])
            }],
            "payer":      {"email": usuario.email},
            "metadata":   {"usuario_id": usuario.id, "plano": plano},
            "back_urls":  {
                "success": f"{BASE_URL}/sucesso",
                "failure": f"{BASE_URL}/falha",
                "pending": f"{BASE_URL}/pendente"
            },
            "notification_url": f"{BASE_URL}/webhook/mercadopago",
            "auto_return": "approved"
        }
        pref     = sdk.preference().create(preference_data)
        pagamento = Pagamento(
            usuario_id=usuario.id,
            plano=plano,
            valor=float(PRECOS[plano]["valor"]),
            status="pendente"
        )
        db.add(pagamento)
        db.commit()
        return RedirectResponse(url=pref["response"]["init_point"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/webhook/mercadopago")
async def webhook_mp(request: Request, db: Session = Depends(get_db)):
    try:
        data    = await request.json()
        tipo    = data.get("type", "")
        if tipo == "payment":
            mp_id   = str(data.get("data", {}).get("id", ""))
            sdk     = mercadopago.SDK(MP_ACCESS_TOKEN)
            payment = sdk.payment().get(mp_id)
            info    = payment["response"]
            status  = info.get("status", "")
            meta    = info.get("metadata", {})
            uid     = meta.get("usuario_id")
            plano   = meta.get("plano", "premium")
            if status == "approved" and uid:
                usuario = db.query(Usuario).filter(Usuario.id == uid).first()
                if usuario:
                    usuario.plano = plano
                    db.commit()
                    adicionar_pontos(usuario, 50, db)
                    pagamento = db.query(Pagamento).filter(
                        Pagamento.usuario_id == uid,
                        Pagamento.status == "pendente"
                    ).first()
                    if pagamento:
                        pagamento.status = "aprovado"
                        pagamento.mp_id  = mp_id
                        db.commit()
                    import asyncio
                    asyncio.create_task(
                        enviar_email_premium(usuario.nome, usuario.email, plano)
                    )
        return {"status": "ok"}
    except Exception as e:
        print(f"Erro webhook: {e}")
        return {"status": "error"}

# ================================================================
# ROTAS — ADMIN COMPLETO
# ================================================================

@app.get("/admin", response_class=HTMLResponse)
def admin(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario or usuario.email != ADMIN_EMAIL:
        return RedirectResponse(url="/")
    todos          = db.query(Usuario).all()
    total_analises = db.query(Analise).count()
    total_msgs     = db.query(Mensagem).count()
    total_diarios  = db.query(Diario).count()
    total_logs     = db.query(LogAcesso).count()
    pagamentos     = db.query(Pagamento).filter(
        Pagamento.status == "aprovado"
    ).all()
    premium        = [u for u in todos if u.plano == "premium"]
    enterprise     = [u for u in todos if u.plano == "enterprise"]
    trial          = [u for u in todos if u.plano == "trial"]
    free           = [u for u in todos if u.plano == "free"]
    receita        = sum(
        49 if p.plano == "premium" else 199
        for p in pagamentos
    )
    logs_recentes  = db.query(LogAcesso).order_by(
        LogAcesso.criado_em.desc()
    ).limit(50).all()
    lista = [{
        "id":            u.id,
        "nome":          u.nome,
        "email":         u.email,
        "plano":         u.plano,
        "pontos":        u.pontos,
        "badge":         u.badge,
        "total_analises":len(u.analises),
        "criado_em":     u.criado_em.strftime("%d/%m/%Y"),
        "ativo":         u.ativo,
        "ref_code":      u.ref_code,
        "indicado_por":  u.indicado_por,
        "trial_usado":   u.trial_usado
    } for u in todos]
    return templates.TemplateResponse(request, "admin.html", {
        "usuario":           usuario,
        "usuarios":          lista,
        "total_usuarios":    len(todos),
        "usuarios_free":     len(free),
        "usuarios_trial":    len(trial),
        "usuarios_premium":  len(premium),
        "usuarios_enterprise":len(enterprise),
        "total_analises":    total_analises,
        "total_msgs":        total_msgs,
        "total_diarios":     total_diarios,
        "total_logs":        total_logs,
        "receita":           receita,
        "logs_recentes":     logs_recentes
    })

@app.post("/admin/usuario/{uid}/plano")
def admin_mudar_plano(uid: int, plano: str = Form(...),
                      request: Request = None, db: Session = Depends(get_db)):
    admin = get_usuario_logado(request, db)
    if not admin or admin.email != ADMIN_EMAIL:
        raise HTTPException(status_code=403, detail="Acesso negado")
    usuario = db.query(Usuario).filter(Usuario.id == uid).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    usuario.plano = plano
    db.commit()
    return {"mensagem": f"Plano de {usuario.nome} alterado para {plano}"}

@app.post("/admin/usuario/{uid}/toggle")
def admin_toggle_usuario(uid: int, request: Request,
                         db: Session = Depends(get_db)):
    admin = get_usuario_logado(request, db)
    if not admin or admin.email != ADMIN_EMAIL:
        raise HTTPException(status_code=403, detail="Acesso negado")
    usuario = db.query(Usuario).filter(Usuario.id == uid).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    usuario.ativo = not usuario.ativo
    db.commit()
    status = "ativado" if usuario.ativo else "desativado"
    return {"mensagem": f"Usuário {usuario.nome} {status}"}

@app.delete("/admin/usuario/{uid}")
def admin_deletar_usuario(uid: int, request: Request,
                          db: Session = Depends(get_db)):
    admin = get_usuario_logado(request, db)
    if not admin or admin.email != ADMIN_EMAIL:
        raise HTTPException(status_code=403, detail="Acesso negado")
    if uid == admin.id:
        raise HTTPException(status_code=400, detail="Não pode deletar a si mesmo")
    usuario = db.query(Usuario).filter(Usuario.id == uid).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    db.delete(usuario)
    db.commit()
    return {"mensagem": f"Usuário deletado com sucesso"}

@app.post("/admin/relatorio/{uid}")
async def admin_enviar_relatorio(uid: int, request: Request,
                                 db: Session = Depends(get_db)):
    admin = get_usuario_logado(request, db)
    if not admin or admin.email != ADMIN_EMAIL:
        raise HTTPException(status_code=403, detail="Acesso negado")
    usuario = db.query(Usuario).filter(Usuario.id == uid).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    await enviar_relatorio_semanal(usuario, db)
    return {"mensagem": f"Relatório enviado para {usuario.email}"}

# ================================================================
# ROTAS — API PÚBLICA COM TOKEN
# ================================================================

def verificar_token(x_api_token: str = Header(None), db: Session = Depends(get_db)):
    if not x_api_token:
        raise HTTPException(status_code=401, detail="Token não fornecido")
    usuario = db.query(Usuario).filter(
        Usuario.api_token == x_api_token,
        Usuario.ativo == True
    ).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="Token inválido")
    return usuario

@app.get("/api/v1/analyze")
def api_analyze(text: str, usuario: Usuario = Depends(verificar_token),
                db: Session = Depends(get_db)):
    if usuario.plano == "free":
        if contar_hoje(Analise, usuario.id, db) >= LIMITES["free"]["analises"]:
            raise HTTPException(status_code=429, detail="Limite atingido")
    emocao      = detectar_emocao(text)
    intensidade = calcular_intensidade(text)
    analise = Analise(
        texto=text, emocao=emocao.capitalize(),
        emoji=get_emoji(emocao),
        recomendacao=recomendacoes.get(emocao, ""),
        intensidade=intensidade,
        usuario_id=usuario.id
    )
    db.add(analise)
    db.commit()
    adicionar_pontos(usuario, 5, db)
    return {
        "emocao":       emocao.capitalize(),
        "emoji":        get_emoji(emocao),
        "recomendacao": recomendacoes.get(emocao, ""),
        "intensidade":  intensidade,
        "timestamp":    datetime.now().isoformat()
    }

@app.get("/api/v1/stats")
def api_stats(usuario: Usuario = Depends(verificar_token),
              db: Session = Depends(get_db)):
    analises = db.query(Analise).filter(Analise.usuario_id == usuario.id).all()
    emocoes  = [a.emocao.lower() for a in analises]
    contagem = {}
    for e in emocoes:
        contagem[e] = contagem.get(e, 0) + 1
    return {
        "usuario":           usuario.nome,
        "plano":             usuario.plano,
        "pontos":            usuario.pontos,
        "badge":             usuario.badge,
        "total_analises":    len(analises),
        "emocoes":           contagem,
        "mais_frequente":    max(contagem, key=contagem.get) if contagem else None
    }

# ================================================================
# ROTAS — PAGAMENTO RETORNO
# ================================================================

@app.get("/sucesso", response_class=HTMLResponse)
async def sucesso(background_tasks: BackgroundTasks,
                  request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if usuario and usuario.plano not in ["premium","enterprise"]:
        usuario.plano = "premium"
        db.commit()
        adicionar_pontos(usuario, 50, db)
        background_tasks.add_task(enviar_email_premium, usuario.nome, usuario.email)
    return HTMLResponse("""
    <html><head><meta charset='UTF-8'>
    <style>
    body{font-family:sans-serif;background:linear-gradient(135deg,#0f0c29,#302b63);
    color:#fff;text-align:center;padding-top:80px}
    h1{font-size:48px;margin-bottom:20px}
    p{font-size:20px;margin-bottom:30px}
    a{background:linear-gradient(90deg,#00d2ff,#3a7bd5);padding:15px 40px;
    border-radius:15px;color:#fff;text-decoration:none;font-size:18px}
    </style></head><body>
    <h1>✅ Pagamento aprovado!</h1>
    <p>Plano Premium ativado com sucesso! 🎉<br>
    Você ganhou <strong>50 pontos</strong> de bônus! 🏆</p>
    <a href='/'>Ir para o Dashboard</a>
    </body></html>""")

@app.get("/falha", response_class=HTMLResponse)
def falha(request: Request):
    return HTMLResponse("""
    <html><head><meta charset='UTF-8'>
    <style>
    body{font-family:sans-serif;background:linear-gradient(135deg,#0f0c29,#302b63);
    color:#fff;text-align:center;padding-top:80px}
    h1{font-size:48px;margin-bottom:20px}
    a{background:#e74c3c;padding:15px 40px;border-radius:15px;
    color:#fff;text-decoration:none;font-size:18px}
    </style></head><body>
    <h1>❌ Pagamento falhou!</h1>
    <p style='font-size:20px;margin-bottom:30px'>
    Tente novamente ou entre em contato com o suporte.</p>
    <a href='/planos'>Tentar novamente</a>
    </body></html>""")

@app.get("/pendente", response_class=HTMLResponse)
def pendente(request: Request):
    return HTMLResponse("""
    <html><head><meta charset='UTF-8'>
    <style>
    body{font-family:sans-serif;background:linear-gradient(135deg,#0f0c29,#302b63);
    color:#fff;text-align:center;padding-top:80px}
    h1{font-size:48px;margin-bottom:20px}
    a{background:#f39c12;padding:15px 40px;border-radius:15px;
    color:#fff;text-decoration:none;font-size:18px}
    </style></head><body>
    <h1>⏳ Pagamento pendente!</h1>
    <p style='font-size:20px;margin-bottom:30px'>
    Assim que confirmado, seu plano será ativado automaticamente!</p>
    <a href='/'>Voltar ao Dashboard</a>
    </body></html>""")
