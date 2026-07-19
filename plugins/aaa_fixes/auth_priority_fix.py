from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from pathlib import Path
from datetime import datetime
import json
import hashlib
import hmac
import base64
import time
import os
import uuid

router = APIRouter(prefix="/api/v1/auth", tags=["Auth Priority Fix"])

ARQ = Path("auth_users_priority.json")
JWT_SECRET = os.getenv("JWT_SECRET", "emotion_platform_secret_2024_albert")


def _load():
    if ARQ.exists():
        try:
            return json.loads(ARQ.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def _save(data):
    ARQ.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def _hash(senha: str) -> str:
    return hashlib.sha256((JWT_SECRET + senha).encode()).hexdigest()


def _b64(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode().rstrip("=")


def _token(uid: str, email: str, plano: str = "free") -> str:
    header = _b64(json.dumps({"alg": "HS256", "typ": "JWT"}).encode())
    payload_data = {
        "sub": uid,
        "email": email,
        "plano": plano,
        "exp": int(time.time()) + 604800
    }
    payload = _b64(json.dumps(payload_data).encode())
    sig = _b64(hmac.new(JWT_SECRET.encode(), f"{header}.{payload}".encode(), hashlib.sha256).digest())
    return f"ep_{header}.{payload}.{sig}"


def _parse_token(token: str):
    if token.startswith("Bearer "):
        token = token.replace("Bearer ", "", 1)
    if token.startswith("ep_"):
        token = token[3:]
    try:
        header, payload, sig = token.split(".")
        expected = _b64(hmac.new(JWT_SECRET.encode(), f"{header}.{payload}".encode(), hashlib.sha256).digest())
        if not hmac.compare_digest(sig, expected):
            return None
        padded = payload + "=" * (-len(payload) % 4)
        data = json.loads(base64.urlsafe_b64decode(padded.encode()).decode())
        if int(data.get("exp", 0)) < int(time.time()):
            return None
        return data
    except Exception:
        return None


@router.post("/cadastrar")
async def cadastrar(request: Request):
    try:
        body = await request.json()
    except Exception:
        body = {}

    nome = (body.get("nome") or body.get("name") or body.get("username") or "").strip()
    if not nome and email:
        nome = email.split("@")[0]
    email = (body.get("email") or "").strip().lower()
    senha = body.get("senha") or ""
    tipo = body.get("tipo") or "paciente"
    telefone = body.get("telefone") or ""

    if len(nome) < 1:
        raise HTTPException(status_code=400, detail="Por favor, informe seu nome")
    if "@" not in email:
        raise HTTPException(status_code=400, detail="E-mail inválido")
    if len(senha) < 6:
        raise HTTPException(status_code=400, detail="Senha mínima: 6 caracteres")

    users = _load()

    if email in users:
        user = users[email]
        token = _token(user["id"], email, user.get("plano", "free"))
        return JSONResponse({
            "status": "ja_cadastrado",
            "user_id": user["id"],
            "nome": user.get("nome", nome),
            "email": email,
            "tipo": user.get("tipo", tipo),
            "plano": user.get("plano", "free"),
            "token": token,
            "access_token": token
        })

    uid = str(uuid.uuid4())[:8]
    users[email] = {
        "id": uid,
        "nome": nome,
        "email": email,
        "senha_hash": _hash(senha),
        "tipo": tipo,
        "telefone": telefone,
        "plano": "free",
        "criado_em": datetime.utcnow().isoformat()
    }
    _save(users)

    token = _token(uid, email, "free")
    return JSONResponse({
        "status": "cadastrado",
        "user_id": uid,
        "nome": nome,
        "email": email,
        "tipo": tipo,
        "plano": "free",
        "token": token,
        "access_token": token
    })


@router.post("/login")
async def login(request: Request):
    try:
        body = await request.json()
    except Exception:
        body = {}

    email = (body.get("email") or "").strip().lower()
    senha = body.get("senha") or ""

    users = _load()
    user = users.get(email)

    if not user:
        raise HTTPException(status_code=401, detail="E-mail não encontrado")

    if user.get("senha_hash") != _hash(senha):
        raise HTTPException(status_code=401, detail="Senha incorreta")

    token = _token(user["id"], email, user.get("plano", "free"))
    return JSONResponse({
        "status": "logado",
        "user_id": user["id"],
        "nome": user.get("nome", ""),
        "email": email,
        "tipo": user.get("tipo", "paciente"),
        "plano": user.get("plano", "free"),
        "token": token,
        "access_token": token
    })


@router.get("/me")
async def me(request: Request):
    auth = request.headers.get("Authorization", "")
    data = _parse_token(auth)

    if not data:
        raise HTTPException(status_code=401, detail="Token inválido")

    users = _load()
    email = data.get("email", "").lower()
    user = users.get(email)

    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return JSONResponse({
        "id": user["id"],
        "nome": user.get("nome", ""),
        "email": email,
        "tipo": user.get("tipo", "paciente"),
        "plano": user.get("plano", "free")
    })


@router.post("/refresh")
async def refresh(request: Request):
    auth = request.headers.get("Authorization", "")
    data = _parse_token(auth)
    if not data:
        raise HTTPException(status_code=401, detail="Token inválido")
    token = _token(data["sub"], data["email"], data.get("plano", "free"))
    return JSONResponse({"token": token, "access_token": token})


@router.get("/stats/usuarios")
async def stats():
    users = _load()
    return JSONResponse({
        "total_usuarios": len(users),
        "plataforma": "Emotion Intelligence Platform",
        "auth": "priority_fix"
    })


class Plugin(PluginBase):
    name = "aaa_auth_priority_fix"
    def setup(self, app):
        app.include_router(router)


plugin = Plugin()
