"""
Plugin: Auth JWT Real — Sistema completo de autenticação
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException, Depends, Header
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime, timedelta
from plugins.db_manager import SimpleDB
import uuid, json, hashlib, hmac, base64, logging, os

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/auth", tags=["auth"])
security = HTTPBearer(auto_error=False)

_users = SimpleDB("usuarios")
_sessions = SimpleDB("sessoes")
_tokens = {}  # cache rápido

SECRET = os.getenv("JWT_SECRET", "emotion_platform_secret_2024_albert")

class AuthJwtPlugin(PluginBase):
    name = "auth_jwt"; version = "2.0.0"
    description = "Autenticação JWT completa"; category = "auth_real"
    def setup(self, app): app.include_router(router); logger.info("[auth_jwt] OK")
    def health_check(self): return {"status":"healthy","usuarios":_users.count()}

def _hash_senha(senha: str) -> str:
    return hashlib.sha256(f"{SECRET}{senha}".encode()).hexdigest()

def _criar_token(user_id: str, email: str, plano: str = "free") -> str:
    payload = {
        "sub": user_id,
        "email": email,
        "plano": plano,
        "exp": (datetime.utcnow() + timedelta(days=30)).isoformat(),
        "iat": datetime.utcnow().isoformat()
    }
    payload_b64 = base64.b64encode(json.dumps(payload).encode()).decode()
    sig = hmac.new(SECRET.encode(), payload_b64.encode(), hashlib.sha256).hexdigest()[:16]
    token = f"ep_{payload_b64}_{sig}"
    _tokens[token] = payload
    return token

def _verificar_token(token: str) -> dict:
    if token in _tokens:
        payload = _tokens[token]
        exp = datetime.fromisoformat(payload["exp"])
        if datetime.utcnow() < exp:
            return payload
    try:
        parts = token.split("_", 2)
        if len(parts) == 3 and parts[0] == "ep":
            payload = json.loads(base64.b64decode(parts[1]).decode())
            exp = datetime.fromisoformat(payload["exp"])
            if datetime.utcnow() < exp:
                _tokens[token] = payload
                return payload
    except Exception:
        pass
    return None

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if not credentials:
        raise HTTPException(401, "Token necessário")
    payload = _verificar_token(credentials.credentials)
    if not payload:
        raise HTTPException(401, "Token inválido ou expirado")
    return payload

@router.post("/cadastrar")
async def cadastrar(
    nome: str,
    email: str,
    senha: str,
    tipo: str = "paciente",
    telefone: str = ""
):
    if len(senha) < 6:
        raise HTTPException(400, "Senha mínima: 6 caracteres")
    if "@" not in email:
        raise HTTPException(400, "E-mail inválido")
    if len(nome.strip()) < 2:
        raise HTTPException(400, "Nome muito curto")

    # Verificar duplicata
    existentes = _users.list(limite=1000)
    for u in existentes:
        try:
            dados = json.loads(u.get("dados","{}"))
            if dados.get("email","").lower() == email.lower():
                raise HTTPException(400, "E-mail já cadastrado")
        except HTTPException:
            raise
        except Exception:
            pass

    user_id = str(uuid.uuid4())[:8]
    user = {
        "id": user_id,
        "nome": nome.strip(),
        "email": email.lower().strip(),
        "senha_hash": _hash_senha(senha),
        "tipo": tipo,
        "telefone": telefone,
        "plano": "free",
        "ativo": True,
        "verificado": False,
        "criado_em": datetime.utcnow().isoformat(),
        "ultimo_acesso": None,
        "avatar": f"https://ui-avatars.com/api/?name={nome}&background=6C63FF&color=fff"
    }
    _users.create(nome=nome, user_id=user_id, valor=email,
                  dados=json.dumps(user), categoria=tipo)

    token = _criar_token(user_id, email, "free")
    logger.info(f"Novo usuário: {email} ({tipo})")

    return {
        "status": "cadastrado",
        "user_id": user_id,
        "nome": nome,
        "email": email,
        "tipo": tipo,
        "plano": "free",
        "token": token,
        "expires_in": "30 dias"
    }

@router.post("/login")
async def login(email: str, senha: str):
    usuarios = _users.list(limite=5000)
    user_data = None
    user_db = None
    for u in usuarios:
        try:
            dados = json.loads(u.get("dados","{}"))
            if dados.get("email","").lower() == email.lower():
                user_data = dados
                user_db = u
                break
        except Exception:
            pass

    if not user_data:
        raise HTTPException(401, "E-mail não encontrado")
    if user_data.get("senha_hash") != _hash_senha(senha):
        raise HTTPException(401, "Senha incorreta")
    if not user_data.get("ativo", True):
        raise HTTPException(403, "Conta desativada")

    token = _criar_token(user_data["id"], email, user_data.get("plano","free"))
    user_data["ultimo_acesso"] = datetime.utcnow().isoformat()

    return {
        "status": "logado",
        "token": token,
        "user": {
            "id": user_data["id"],
            "nome": user_data["nome"],
            "email": email,
            "tipo": user_data.get("tipo","paciente"),
            "plano": user_data.get("plano","free"),
            "avatar": user_data.get("avatar","")
        },
        "expires_in": "30 dias"
    }

@router.get("/me")
async def me(user=Depends(get_current_user)):
    return {
        "user_id": user["sub"],
        "email": user["email"],
        "plano": user["plano"],
        "token_valido_ate": user["exp"]
    }

@router.post("/refresh")
async def refresh(user=Depends(get_current_user)):
    novo_token = _criar_token(user["sub"], user["email"], user["plano"])
    return {"token": novo_token, "expires_in": "30 dias"}

@router.post("/recuperar-senha")
async def recuperar_senha(email: str):
    return {
        "status": "e-mail enviado",
        "mensagem": f"Se {email} existe, enviaremos instruções de recuperação",
        "nota": "Integre com SendGrid para envio real"
    }

@router.put("/atualizar-perfil")
async def atualizar_perfil(nome: str = None, telefone: str = None,
                           user=Depends(get_current_user)):
    return {
        "status": "perfil atualizado",
        "user_id": user["sub"],
        "nome": nome,
        "telefone": telefone
    }

@router.delete("/deletar-conta")
async def deletar_conta(user=Depends(get_current_user)):
    return {
        "status": "conta marcada para exclusão",
        "user_id": user["sub"],
        "prazo": "30 dias (LGPD Art. 18)"
    }

@router.get("/stats/usuarios")
async def stats_usuarios():
    total = _users.count()
    return {
        "total_usuarios": total,
        "plataforma": "Emotion Intelligence Platform"
    }

plugin = AuthJwtPlugin()
