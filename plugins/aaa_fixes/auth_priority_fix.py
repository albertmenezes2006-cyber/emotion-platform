from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import hashlib, hmac, base64, time, os, uuid, json
import psycopg2
from urllib.parse import urlparse

router = APIRouter(prefix="/api/v1/auth", tags=["Auth"])

JWT_SECRET = os.getenv("JWT_SECRET", "emotion_platform_secret_2024_albert")
DATABASE_URL = os.getenv("DATABASE_URL", "")

def get_conn():
    url = DATABASE_URL.replace("postgres://", "postgresql://")
    return psycopg2.connect(url, sslmode="require", connect_timeout=10)

def init_table():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS auth_usuarios (
                id VARCHAR(8) PRIMARY KEY,
                nome VARCHAR(500),
                email VARCHAR(500) UNIQUE,
                senha_hash VARCHAR(500),
                tipo VARCHAR(50) DEFAULT 'paciente',
                telefone VARCHAR(50) DEFAULT '',
                plano VARCHAR(50) DEFAULT 'free',
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        pass

init_table()

def _hash(senha):
    return hashlib.sha256((JWT_SECRET + senha).encode()).hexdigest()

def _b64(data):
    return base64.urlsafe_b64encode(data).decode().rstrip("=")

def _token(uid, email, plano="free"):
    header = _b64(json.dumps({"alg":"HS256","typ":"JWT"}).encode())
    payload = _b64(json.dumps({"sub":uid,"email":email,"plano":plano,"exp":int(time.time())+604800}).encode())
    sig = _b64(hmac.new(JWT_SECRET.encode(), f"{header}.{payload}".encode(), hashlib.sha256).digest())
    return f"ep_{header}.{payload}.{sig}"

def _parse_token(token):
    if token.startswith("Bearer "): token = token[7:]
    if token.startswith("ep_"): token = token[3:]
    try:
        header, payload, sig = token.split(".")
        expected = _b64(hmac.new(JWT_SECRET.encode(), f"{header}.{payload}".encode(), hashlib.sha256).digest())
        if not hmac.compare_digest(sig, expected): return None
        data = json.loads(base64.urlsafe_b64decode(payload + "=" * (-len(payload) % 4)).decode())
        if int(data.get("exp",0)) < int(time.time()): return None
        return data
    except: return None

def get_user_by_email(email):
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT id,nome,email,senha_hash,tipo,plano FROM auth_usuarios WHERE email=%s", (email,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row:
            return {"id":row[0],"nome":row[1],"email":row[2],"senha_hash":row[3],"tipo":row[4],"plano":row[5]}
    except: pass
    return None

def create_user(uid, nome, email, senha_hash, tipo, telefone):
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO auth_usuarios (id,nome,email,senha_hash,tipo,telefone,plano)
            VALUES (%s,%s,%s,%s,%s,%s,'free')
        """, (uid, nome, email, senha_hash, tipo, telefone))
        conn.commit()
        cur.close()
        conn.close()
        return True
    except: return False

@router.post("/cadastrar")
async def cadastrar(request: Request):
    try: body = await request.json()
    except: body = {}
    email = (body.get("email") or "").strip().lower()
    senha = body.get("senha") or ""
    tipo = body.get("tipo") or "paciente"
    telefone = body.get("telefone") or ""
    nome = (body.get("nome") or body.get("name") or "").strip()
    if not nome: nome = email.split("@")[0] if email else "Usuario"
    if "@" not in email: raise HTTPException(400, "E-mail invalido")
    if len(senha) < 6: raise HTTPException(400, "Senha minima: 6 caracteres")
    existing = get_user_by_email(email)
    if existing:
        token = _token(existing["id"], email, existing["plano"])
        return JSONResponse({"status":"ja_cadastrado","user_id":existing["id"],"nome":existing["nome"],"email":email,"tipo":existing["tipo"],"plano":existing["plano"],"token":token,"access_token":token})
    uid = str(uuid.uuid4())[:8]
    ok = create_user(uid, nome, email, _hash(senha), tipo, telefone)
    if not ok: raise HTTPException(500, "Erro ao criar conta")
    token = _token(uid, email, "free")
    return JSONResponse({"status":"cadastrado","user_id":uid,"nome":nome,"email":email,"tipo":tipo,"plano":"free","token":token,"access_token":token})

@router.post("/login")
async def login(request: Request):
    try: body = await request.json()
    except: body = {}
    email = (body.get("email") or "").strip().lower()
    senha = body.get("senha") or ""
    user = get_user_by_email(email)
    if not user: raise HTTPException(401, "E-mail nao encontrado")
    if user["senha_hash"] != _hash(senha): raise HTTPException(401, "Senha incorreta")
    token = _token(user["id"], email, user["plano"])
    return JSONResponse({"status":"logado","user_id":user["id"],"nome":user["nome"],"email":email,"tipo":user["tipo"],"plano":user["plano"],"token":token,"access_token":token})

@router.get("/me")
async def me(request: Request):
    auth = request.headers.get("Authorization","")
    data = _parse_token(auth)
    if not data: raise HTTPException(401, "Token invalido")
    user = get_user_by_email(data.get("email",""))
    if not user: raise HTTPException(404, "Usuario nao encontrado")
    return JSONResponse({"id":user["id"],"nome":user["nome"],"email":user["email"],"tipo":user["tipo"],"plano":user["plano"]})

@router.post("/refresh")
async def refresh(request: Request):
    auth = request.headers.get("Authorization","")
    data = _parse_token(auth)
    if not data: raise HTTPException(401, "Token invalido")
    token = _token(data["sub"], data["email"], data.get("plano","free"))
    return JSONResponse({"token":token,"access_token":token})

@router.get("/stats/usuarios")
async def stats():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM auth_usuarios")
        total = cur.fetchone()[0]
        cur.close()
        conn.close()
        return JSONResponse({"total_usuarios":total,"auth":"supabase"})
    except: return JSONResponse({"total_usuarios":0,"auth":"supabase_erro"})

class Plugin(PluginBase):
    name = "aaa_auth_priority_fix"
    def setup(self, app): app.include_router(router)

plugin = Plugin()
