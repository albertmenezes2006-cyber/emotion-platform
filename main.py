from fastapi import FastAPI, HTTPException, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from passlib.context import CryptContext
from datetime import datetime
import unicodedata
import mercadopago
import os
from dotenv import load_dotenv

load_dotenv()
MP_ACCESS_TOKEN = os.getenv("MP_ACCESS_TOKEN")

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

app = FastAPI(title="Emotion Intelligence Platform", version="5.0")
templates = Jinja2Templates(directory="templates")
sessoes = {}

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
             "beijo", "afetuoso", "estima", "quero"]
}

recomendacoes = {
    "alegria": "Continue assim! Compartilhe sua energia positiva! 🌟",
    "tristeza": "Considere conversar com alguém de confiança. 💙",
    "raiva": "Respire fundo. Uma pausa pode ajudar muito. 🌬️",
    "medo": "Identifique a causa do medo. Busque apoio se precisar. 🤝",
    "surpresa": "Absorva o momento! Surpresas fazem parte da vida. ✨",
    "nojo": "Afaste-se do que causa desconforto. Cuide-se. 🛡️",
    "amor": "O amor enriquece a vida. Valorize seus sentimentos. ❤️",
    "neutro": "Momento de equilíbrio. Aproveite a calma! ⚖️"
}

def get_emoji(emocao):
    emojis = {
        "alegria": "😄", "tristeza": "😢", "raiva": "😡",
        "medo": "😨", "surpresa": "😲", "nojo": "🤢",
        "amor": "❤️", "neutro": "😐"
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
        return RedirectResponse(url="/login")
    return templates.TemplateResponse(request, "dashboard.html", {"usuario": usuario})

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
def cadastro(request: Request, nome: str = Form(...), email: str = Form(...), senha: str = Form(...), db: Session = Depends(get_db)):
    existe = db.query(Usuario).filter(Usuario.email == email).first()
    if existe:
        return templates.TemplateResponse(request, "cadastro.html", {"erro": "Email já cadastrado"})
    novo = Usuario(nome=nome, email=email, senha=hash_senha(senha), plano="free")
    db.add(novo)
    db.commit()
    return RedirectResponse(url="/login", status_code=302)

@app.get("/logout")
def logout(request: Request):
    session_id = request.cookies.get("session_id")
    if session_id in sessoes:
        del sessoes[session_id]
    response = RedirectResponse(url="/login")
    response.delete_cookie("session_id")
    return response

@app.get("/analyze")
def analyze(request: Request, text: str, db: Session = Depends(get_db)):
    usuario = get_usuario_logado(request, db)
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autorizado")
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

@app.get("/sucesso", response_class=HTMLResponse)
def sucesso(request: Request):
    return HTMLResponse("<h1 style='color:green;font-family:sans-serif;text-align:center;margin-top:100px'>✅ Pagamento aprovado! Obrigado!</h1><br><center><a href='/'>Voltar ao Dashboard</a></center>")

@app.get("/falha", response_class=HTMLResponse)
def falha(request: Request):
    return HTMLResponse("<h1 style='color:red;font-family:sans-serif;text-align:center;margin-top:100px'>❌ Pagamento falhou. Tente novamente.</h1><br><center><a href='/planos'>Tentar novamente</a></center>")

@app.get("/pendente", response_class=HTMLResponse)
def pendente(request: Request):
    return HTMLResponse("<h1 style='color:orange;font-family:sans-serif;text-align:center;margin-top:100px'>⏳ Pagamento pendente. Aguarde a confirmação.</h1><br><center><a href='/'>Voltar ao Dashboard</a></center>")

