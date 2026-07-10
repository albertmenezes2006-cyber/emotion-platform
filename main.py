from fastapi import FastAPI, HTTPException, Request, Depends, Form, BackgroundTasks
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from passlib.context import CryptContext
from datetime import datetime, date
import unicodedata
import mercadopago
import sendgrid
from sendgrid.helpers.mail import Mail
import os

MP_ACCESS_TOKEN = "APP_USR-4193087911174356-070916-cefe9e3636798457e9e78f6036cd4500-3532571592"
ADMIN_EMAIL = "albertmenezes2006@gmail.com"
SENDGRID_API_KEY = "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"

DATABASE_URL = "sqlite:///./emotion.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    senha = Column(String, nullable=False)
    plano = Column(String, default="free")
    criado_em = Column(DateTime, default=datetime.now)
    analises = relationship("Analise", back_populates="usuario")

class Analise(Base):
    __tablename__ = "analises"
    id = Column(Integer, primary_key=True, index=True)
    texto = Column(String, nullable=False)
    emocao = Column(String, nullable=False)
    emoji = Column(String, nullable=False)
    recomendacao = Column(String, nullable=False)
    criado_em = Column(DateTime, default=datetime.now)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    usuario = relationship("Usuario", back_populates="analises")

Base.metadata.create_all(bind=engine)

pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")

def hash_senha(senha):
    return pwd_context.hash(senha)

def verificar_senha(senha, hash):
    return pwd_context.verify(senha, hash)

app = FastAPI(title="Emotion Intelligence Platform", version="9.0")
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
sessoes = {}
LIMITE_FREE = 10

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
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def contar_analises_hoje(usuario_id: int, db: Session):
    hoje = date.today()
    return db.query(Analise).filter(
        Analise.usuario_id == usuario_id,
        Analise.criado_em >= datetime.combine(hoje, datetime.min.time())
    ).count()

async def enviar_email_boas_vindas(nome: str, email: str):
    try:
        sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
        message = Mail(
            from_email=ADMIN_EMAIL,
            to_emails=email,
            subject="🧠 Bem-vindo ao Emotion Intelligence Platform!",
            html_content=f"""
            <html><body style="font-family:sans-serif;padding:40px">
            <h1 style="color:#00d2ff">🧠 Emotion Intelligence</h1>
            <h2>Olá, {nome}! 👋</h2>
            <p style="font-size:18px">Bem-vindo à plataforma de inteligência emocional!</p>
            <br>
            <p>Com o seu plano FREE você pode:</p>
            <ul>
            <li>✅ 10 análises por dia</li>
            <li>✅ Histórico de análises</li>
            <li>✅ Estatísticas emocionais</li>
            <li>✅ Análise por voz</li>
            </ul>
            <br>
            <a href="https://emotion-platform-albert.onrender.com/planos"
            style="background:#00d2ff;padding:15px 30px;border-radius:15px;color:#fff;text-decoration:none;font-size:16px">
            🚀 Ver Planos Premium
            </a>
            <br><br>
            <p style="color:#666;font-size:12px">Emotion Intelligence Platform © 2026</p>
            </body></html>
            """
        )
        sg.send(message)
        print(f"Email boas-vindas enviado para {email}")
    except Exception as e:
        print(f"Erro email: {e}")

async def enviar_email_premium(nome: str, email: str):
    try:
        sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
        message = Mail(
            from_email=ADMIN_EMAIL,
            to_emails=email,
            subject="⭐ Seu plano Premium está ativo!",
            html_content=f"""
            <html><body style="font-family:sans-serif;padding:40px">
            <h1 style="color:#00d2ff">🧠 Emotion Intelligence</h1>
            <h2>Parabéns, {nome}! 🎉</h2>
            <p style="font-size:18px">Seu plano Premium foi ativado com sucesso!</p>
            <br>
            <p>Agora você tem acesso a:</p>
            <ul>
            <li>✅ Análises ilimitadas</li>
            <li>✅ Histórico completo</li>
            <li>✅ Gráficos avançados</li>
            <li>✅ Análise por voz</li>
            <li>✅ Suporte prioritário</li>
            </ul>
            <br>
            <a href="https://emotion-platform-albert.onrender.com"
            style="background:#00d2ff;padding:15px 30px;border-radius:15px;color:#fff;text-decoration:none;font-size:16px">
            🚀 Acessar Dashboard
            </a>
            <br><br>
            <p style="color:#666;font-size:12px">Emotion Intelligence Platform © 2026</p>
            </body></html>
            """
        )
        sg.send(message)
        print(f"Email premium enviado para {email}")
    except Exception as e:
        print(f"Erro email: {e}")

palavras_emocoes = {
    "alegria": ["feliz", "alegre", "contente", "animado", "otimo", "maravilhoso",
                "incrivel", "satisfeito", "radiante", "euforico", "empolgado",
                "bem", "prazer", "alegra", "jubilo", "vencedor", "felicidade"],
    "tristeza": ["triste", "deprimido", "chateado", "desanimado", "sozinho",
                 "melancolico", "chorando", "sofrendo", "perdido", "abandonado",
                 "luto", "dor", "pena", "lamento", "chorar"],
    "raiva": ["raiva", "irritado", "furioso", "bravo", "odio", "revoltado",
              "indignado", "nervoso", "estressado", "explosivo",
              "agressivo", "enfurecido", "colera"],
    "medo": ["medo", "assustado", "apavorado", "ansioso", "preocupado",
             "tenso", "inseguro", "receoso", "aterrorizado", "ansiedade",
             "panico", "fobia"],
    "surpresa": ["surpreso", "chocado", "impressionado", "espantado",
                 "uau", "nossa", "caramba", "inacreditavel"],
    "nojo": ["nojo", "repulsa", "asco", "horrivel", "terrivel",
             "repugnante", "enjoado"],
    "amor": ["amo", "amar", "amor", "carinho", "apaixonado", "ternura",
             "beijo", "afetuoso", "estima", "quero"],
    "esperanca": ["esperanca", "esperancoso", "otimista", "acredito",
                  "confiante", "positivo"],
    "gratidao": ["grato", "agradecido", "obrigado", "gratidao",
                 "reconhecido", "valorizando"],
    "solidao": ["sozinho", "isolado", "abandonado", "ninguem", "excluido"],
    "euforia": ["euforico", "empolgado", "animadissimo", "fantastico", "extraordinario"]
}

recomendacoes = {
    "alegria": "Continue assim! Compartilhe sua energia positiva! 🌟",
    "tristeza": "Considere conversar com alguém de confiança. 💙",
    "raiva": "Respire fundo. Uma pausa pode ajudar muito. 🌬️",
    "medo": "Identifique a causa do medo. Busque apoio se precisar. 🤝",
    "surpresa": "Absorva o momento! Surpresas fazem parte da vida. ✨",
    "nojo": "Afaste-se do que causa desconforto. Cuide-se. 🛡️",
    "amor": "O amor enriquece a vida. Valorize seus sentimentos. ❤️",
    "esperanca": "Continue acreditando! O futuro reserva coisas boas. 🌅",
    "gratidao": "A gratidão transforma perspectivas. Continue assim! 🙏",
    "solidao": "Você não está sozinho. Busque conexões significativas. 🤗",
    "euforia": "Aproveite esse momento incrível com responsabilidade! 🎉",
    "neutro": "Momento de equilíbrio. Aproveite a calma! ⚖️"
}

def get_emoji(emocao):
    emojis = {
        "alegria": "😄", "tristeza": "😢", "raiva": "😡",
        "medo": "😨", "surpresa": "😲", "nojo": "🤢",
        "amor": "❤️", "esperanca": "🌅", "gratidao": "🙏",
        "solidao": "😔", "euforia": "🎉", "neutro": "😐"
    }
    return emojis.get(emocao, "😐")

def detectar_emocao(text):
    text_lower = text.lower()
    text_sem_acento = ''.join(
        c for c in unicodedata.normalize('NFD', text_lower)
        if unicodedata.category(c) != 'Mn'
    )
    pontuacao = {}
    for emocao, palavras_list in palavras_emocoes.items():
        pontos = sum(1 for palavra in palavras_list if palavra in text_sem_acento)
        if pontos > 0:
            pontuacao[emocao] = pontos
    if pontuacao:
        return max(pontuacao, key=pontuacao.get)
    return "neutro"

@app.get("/", response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return templates.TemplateResponse(request, "index.html")
    analises_hoje = contar_analises_hoje(usuario.id, db)
    return templates.TemplateResponse(request, "dashboard.html", {
        "usuario": usuario,
        "analises_hoje": analises_hoje,
        "limite_free": LIMITE_FREE
    })

@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(request, "login.html")

@app.post("/login")
def login(request: Request, email: str = Form(...), senha: str = Form(...), db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if not usuario or not verificar_senha(senha, usuario.senha):
        return templates.TemplateResponse(request, "login.html", {"erro": "Email ou senha incorretos"})
    import uuid
    session_id = str(uuid.uuid4())
    sessoes[session_id] = usuario.id
    response = RedirectResponse(url="/", status_code=302)
    response.set_cookie(key="session_id", value=session_id)
    return response

@app.get("/cadastro", response_class=HTMLResponse)
def cadastro_page(request: Request):
    return templates.TemplateResponse(request, "cadastro.html")

@app.post("/cadastro")
async def cadastro(background_tasks: BackgroundTasks, request: Request, nome: str = Form(...), email: str = Form(...), senha: str = Form(...), db: Session = Depends(get_db)):
    existe = db.query(Usuario).filter(Usuario.email == email).first()
    if existe:
        return templates.TemplateResponse(request, "cadastro.html", {"erro": "Email já cadastrado"})
    novo = Usuario(nome=nome, email=email, senha=hash_senha(senha), plano="free")
    db.add(novo)
    db.commit()
    background_tasks.add_task(enviar_email_boas_vindas, nome, email)
    return RedirectResponse(url="/login", status_code=302)

@app.get("/logout")
def logout(request: Request):
    session_id = request.cookies.get("session_id")
    if session_id in sessoes:
        del sessoes[session_id]
    response = RedirectResponse(url="/login")
    response.delete_cookie("session_id")
    return response

@app.get("/perfil", response_class=HTMLResponse)
def perfil_page(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return RedirectResponse(url="/login")
    total_analises = db.query(Analise).filter(Analise.usuario_id == usuario.id).count()
    analises_hoje = contar_analises_hoje(usuario.id, db)
    dias_cadastrado = (datetime.now() - usuario.criado_em).days
    return templates.TemplateResponse(request, "perfil.html", {
        "usuario": usuario,
        "total_analises": total_analises,
        "analises_hoje": analises_hoje,
        "dias_cadastrado": dias_cadastrado
    })

@app.post("/perfil")
def perfil_update(request: Request, nome: str = Form(...), senha: str = Form(""), confirmar_senha: str = Form(""), db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return RedirectResponse(url="/login")
    if senha and senha != confirmar_senha:
        total_analises = db.query(Analise).filter(Analise.usuario_id == usuario.id).count()
        analises_hoje = contar_analises_hoje(usuario.id, db)
        dias_cadastrado = (datetime.now() - usuario.criado_em).days
        return templates.TemplateResponse(request, "perfil.html", {
            "usuario": usuario,
            "total_analises": total_analises,
            "analises_hoje": analises_hoje,
            "dias_cadastrado": dias_cadastrado,
            "erro": "As senhas não coincidem!"
        })
    usuario.nome = nome
    if senha:
        usuario.senha = hash_senha(senha)
    db.commit()
    total_analises = db.query(Analise).filter(Analise.usuario_id == usuario.id).count()
    analises_hoje = contar_analises_hoje(usuario.id, db)
    dias_cadastrado = (datetime.now() - usuario.criado_em).days
    return templates.TemplateResponse(request, "perfil.html", {
        "usuario": usuario,
        "total_analises": total_analises,
        "analises_hoje": analises_hoje,
        "dias_cadastrado": dias_cadastrado,
        "sucesso": "Perfil atualizado com sucesso!"
    })

@app.get("/analyze")
def analyze(request: Request, text: str, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autorizado")
    if usuario.plano == "free":
        analises_hoje = contar_analises_hoje(usuario.id, db)
        if analises_hoje >= LIMITE_FREE:
            raise HTTPException(status_code=429, detail="Limite atingido!")
    emocao = detectar_emocao(text)
    analise = Analise(
        texto=text,
        emocao=emocao.capitalize(),
        emoji=get_emoji(emocao),
        recomendacao=recomendacoes.get(emocao, ""),
        usuario_id=usuario.id
    )
    db.add(analise)
    db.commit()
    return {
        "texto": text,
        "emocao": emocao.capitalize(),
        "emoji": get_emoji(emocao),
        "recomendacao": recomendacoes.get(emocao, ""),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

@app.get("/historico")
def ver_historico(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autorizado")
    analises = db.query(Analise).filter(Analise.usuario_id == usuario.id).all()
    return {
        "total": len(analises),
        "analises": [{"texto": a.texto, "emocao": a.emocao, "emoji": a.emoji,
                      "recomendacao": a.recomendacao,
                      "timestamp": a.criado_em.strftime("%Y-%m-%d %H:%M:%S")} for a in analises]
    }

@app.get("/stats")
def stats(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autorizado")
    analises = db.query(Analise).filter(Analise.usuario_id == usuario.id).all()
    if not analises:
        return {"mensagem": "Nenhuma analise ainda"}
    emocoes = [a.emocao.lower() for a in analises]
    contagem = {}
    for e in emocoes:
        contagem[e] = contagem.get(e, 0) + 1
    return {
        "total_analises": len(analises),
        "emocoes_detectadas": contagem,
        "mais_frequente": max(contagem, key=contagem.get)
    }

@app.get("/planos", response_class=HTMLResponse)
def planos(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return RedirectResponse(url="/login")
    return templates.TemplateResponse(request, "planos.html", {"usuario": usuario})

@app.get("/checkout")
def checkout(request: Request, plano: str, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        return RedirectResponse(url="/login")
    precos = {
        "premium": {"valor": 49, "nome": "Emotion Premium"},
        "enterprise": {"valor": 199, "nome": "Emotion Enterprise"}
    }
    if plano not in precos:
        raise HTTPException(status_code=400, detail="Plano invalido")
    try:
        sdk = mercadopago.SDK(MP_ACCESS_TOKEN)
        preference_data = {
            "items": [{
                "title": precos[plano]["nome"],
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": float(precos[plano]["valor"])
            }],
            "payer": {"email": usuario.email},
            "back_urls": {
                "success": "https://emotion-platform-albert.onrender.com/sucesso",
                "failure": "https://emotion-platform-albert.onrender.com/falha",
                "pending": "https://emotion-platform-albert.onrender.com/pendente"
            },
            "auto_return": "approved"
        }
        preference_response = sdk.preference().create(preference_data)
        preference = preference_response["response"]
        return RedirectResponse(url=preference["init_point"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/admin", response_class=HTMLResponse)
def admin(request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario or usuario.email != ADMIN_EMAIL:
        return RedirectResponse(url="/")
    todos_usuarios = db.query(Usuario).all()
    total_analises = db.query(Analise).count()
    usuarios_premium = len([u for u in todos_usuarios if u.plano == "premium"])
    usuarios_enterprise = len([u for u in todos_usuarios if u.plano == "enterprise"])
    usuarios_free = len([u for u in todos_usuarios if u.plano == "free"])
    receita = (usuarios_premium * 49) + (usuarios_enterprise * 199)
    lista_usuarios = []
    for u in todos_usuarios:
        lista_usuarios.append({
            "nome": u.nome,
            "email": u.email,
            "plano": u.plano,
            "total_analises": len(u.analises),
            "criado_em": u.criado_em.strftime("%d/%m/%Y")
        })
    return templates.TemplateResponse(request, "admin.html", {
        "usuario": usuario,
        "usuarios": lista_usuarios,
        "total_usuarios": len(todos_usuarios),
        "usuarios_free": usuarios_free,
        "usuarios_premium": usuarios_premium,
        "total_analises": total_analises,
        "receita": receita
    })

@app.get("/sucesso", response_class=HTMLResponse)
async def sucesso(background_tasks: BackgroundTasks, request: Request, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if usuario:
        usuario.plano = "premium"
        db.commit()
        background_tasks.add_task(enviar_email_premium, usuario.nome, usuario.email)
    return HTMLResponse("""
    <html><head><meta charset='UTF-8'><style>
    body{font-family:sans-serif;background:linear-gradient(135deg,#0f0c29,#302b63);color:#fff;text-align:center;padding-top:100px}
    h1{font-size:48px;margin-bottom:20px}
    a{background:linear-gradient(90deg,#00d2ff,#3a7bd5);padding:15px 40px;border-radius:15px;color:#fff;text-decoration:none;font-size:18px}
    </style></head><body>
    <h1>✅ Pagamento aprovado!</h1>
    <p style='font-size:20px;margin-bottom:30px'>Plano Premium ativado! Verifique seu email. 📧</p>
    <a href='/'>Ir para o Dashboard</a>
    </body></html>""")

@app.get("/falha", response_class=HTMLResponse)
def falha(request: Request):
    return HTMLResponse("""
    <html><head><meta charset='UTF-8'><style>
    body{font-family:sans-serif;background:linear-gradient(135deg,#0f0c29,#302b63);color:#fff;text-align:center;padding-top:100px}
    h1{font-size:48px;margin-bottom:20px}
    a{background:#e74c3c;padding:15px 40px;border-radius:15px;color:#fff;text-decoration:none;font-size:18px}
    </style></head><body>
    <h1>❌ Pagamento falhou!</h1>
    <a href='/planos'>Tentar novamente</a>
    </body></html>""")

@app.get("/pendente", response_class=HTMLResponse)
def pendente(request: Request):
    return HTMLResponse("""
    <html><head><meta charset='UTF-8'><style>
    body{font-family:sans-serif;background:linear-gradient(135deg,#0f0c29,#302b63);color:#fff;text-align:center;padding-top:100px}
    h1{font-size:48px;margin-bottom:20px}
    a{background:#f39c12;padding:15px 40px;border-radius:15px;color:#fff;text-decoration:none;font-size:18px}
    </style></head><body>
    <h1>⏳ Pagamento pendente!</h1>
    <a href='/'>Voltar ao Dashboard</a>
    </body></html>""")
