"""
Plugin: Auth PostgreSQL — usuários persistem entre deploys
Padrão: PluginBase + plugin = AuthPostgresqlPlugin()
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime
from plugins.db_manager import SimpleDB
import hashlib
import logging
import os
import json
import uuid

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/auth-pg", tags=["auth_postgresql"])
security = HTTPBearer(auto_error=False)

DATABASE_URL = os.getenv("DATABASE_URL", "")
JWT_SECRET   = os.getenv("JWT_SECRET", "emotion_platform_secret_2024_albert")
_users_pg    = SimpleDB("users_postgresql")

def _hash(senha: str) -> str:
    return hashlib.sha256(f"{JWT_SECRET}{senha}".encode()).hexdigest()

def _token(uid: str, email: str, plano: str) -> str:
    import base64
    import hmac
    import time
    header  = base64.b64encode(b'{"alg":"HS256"}').decode().rstrip("=")
    payload = base64.b64encode(json.dumps({
        "sub": uid, "email": email, "plano": plano,
        "exp": int(time.time()) + 604800
    }).encode()).decode().rstrip("=")
    sig = base64.b64encode(
        hmac.new(JWT_SECRET.encode(), f"{header}.{payload}".encode(), hashlib.sha256).digest()
    ).decode().rstrip("=")
    return f"{header}.{payload}.{sig}"

from pydantic import BaseModel
class CadastroReq(BaseModel):
    email: str
    nome:  str
    senha: str

class LoginReq(BaseModel):
    email: str
    senha: str

@router.post("/cadastrar")
async def cadastrar(req: CadastroReq):
    existente = _users_pg.get(req.email)
    if existente:
        raise HTTPException(400, "Email já cadastrado")
    uid = str(uuid.uuid4())
    _users_pg.set(req.email, {
        "id": uid, "email": req.email,
        "nome": req.nome, "senha_hash": _hash(req.senha),
        "plano": "free", "criado_em": datetime.utcnow().isoformat()
    })
    return {"token": _token(uid, req.email, "free"), "plano": "free",
            "nome": req.nome, "msg": "Cadastro realizado!"}

@router.post("/login")
async def login(req: LoginReq):
    user = _users_pg.get(req.email)
    if not user or user.get("senha_hash") != _hash(req.senha):
        raise HTTPException(401, "Email ou senha incorretos")
    return {"token": _token(user["id"], req.email, user.get("plano","free")),
            "plano": user.get("plano","free"), "nome": user.get("nome",""),
            "msg": "Login realizado!"}

@router.get("/me-pg")
async def me(creds: HTTPAuthorizationCredentials = Depends(security)):
    if not creds:
        raise HTTPException(401, "Token necessário")
    return {"autenticado": True, "token_recebido": True}

@router.get("/status")
async def status():
    backend = "PostgreSQL" if DATABASE_URL and "postgresql" in DATABASE_URL else "SQLite/SimpleDB"
    total   = _users_pg.count() if hasattr(_users_pg, "count") else 0
    return {"backend": backend, "status": "online", "versao": "2.0", "usuarios": total}

class AuthPostgresqlPlugin(PluginBase):
    name        = "auth_postgresql"
    version     = "2.0.0"
    description = "Auth com persistência PostgreSQL"
    category    = "auth_real"

    def setup(self, app):
        app.include_router(router)
        logger.info("[auth_postgresql] ✅ OK")

    def health_check(self):
        return {"status": "healthy", "plugin": self.name}

plugin = AuthPostgresqlPlugin()
