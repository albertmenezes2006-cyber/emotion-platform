"""Plugin: Rate Limit — bloqueio após 5 tentativas falhas"""
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime, timedelta
import time

router = APIRouter(prefix="/api/v1/rate-limit", tags=["seguranca"])

# Memória: {ip: {"tentativas": N, "bloqueado_ate": timestamp}}
_tentativas = {}
MAX_TENTATIVAS = 5
BLOQUEAR_MINUTOS = 15

def verificar_rate_limit(ip: str) -> bool:
    """Retorna True se bloqueado"""
    agora = time.time()
    if ip in _tentativas:
        dados = _tentativas[ip]
        if dados.get("bloqueado_ate", 0) > agora:
            return True  # Bloqueado
        if dados.get("tentativas", 0) >= MAX_TENTATIVAS:
            _tentativas[ip]["bloqueado_ate"] = agora + (BLOQUEAR_MINUTOS * 60)
            _tentativas[ip]["tentativas"] = 0
            return True
    return False

def registrar_falha(ip: str):
    """Registra tentativa falha"""
    if ip not in _tentativas:
        _tentativas[ip] = {"tentativas": 0, "bloqueado_ate": 0}
    _tentativas[ip]["tentativas"] += 1

def limpar_ip(ip: str):
    """Limpa tentativas após login bem sucedido"""
    if ip in _tentativas:
        del _tentativas[ip]

@router.get("/status")
async def status():
    return {"plugin": "rate_limit", "categoria": "seguranca",
            "max_tentativas": MAX_TENTATIVAS,
            "bloquear_minutos": BLOQUEAR_MINUTOS,
            "ips_monitorados": len(_tentativas),
            "ts": datetime.utcnow().isoformat()}

@router.get("/listar")
async def listar():
    agora = time.time()
    return {
        "total": len(_tentativas),
        "bloqueados": sum(1 for d in _tentativas.values() if d.get("bloqueado_ate", 0) > agora),
        "items": [
            {"ip": ip, "tentativas": d["tentativas"],
             "bloqueado": d.get("bloqueado_ate", 0) > agora}
            for ip, d in list(_tentativas.items())[-50:]
        ]
    }

@router.post("/criar")
async def criar(request: Request):
    return JSONResponse({"ok": True})

class RateLimitPlugin(PluginBase):
    name = "rate_limit"
    version = "2.0.0"
    description = "Rate limiting com bloqueio real"
    category = "seguranca"

    def setup(self, app):
        app.include_router(router)

        # Adicionar middleware de rate limit
        from fastapi import Request as FastRequest
        from fastapi.responses import JSONResponse as FastJSON
        from starlette.middleware.base import BaseHTTPMiddleware

        class RateLimitMiddleware(BaseHTTPMiddleware):
            async def dispatch(self, request: FastRequest, call_next):
                # Aplicar rate limit apenas em rotas de auth
                if "/auth/login" in request.url.path or "/auth/cadastrar" in request.url.path:
                    ip = request.client.host if request.client else "unknown"
                    if verificar_rate_limit(ip):
                        return FastJSON(
                            {"detail": f"Muitas tentativas. Tente em {BLOQUEAR_MINUTOS} minutos."},
                            status_code=429
                        )

                response = await call_next(request)

                # Registrar falhas de auth
                if response.status_code == 401 and "/auth/login" in request.url.path:
                    ip = request.client.host if request.client else "unknown"
                    registrar_falha(ip)
                elif response.status_code == 200 and "/auth/login" in request.url.path:
                    ip = request.client.host if request.client else "unknown"
                    limpar_ip(ip)

                return response

        app.add_middleware(RateLimitMiddleware)
        import logging
        logging.getLogger(__name__).info("[rate_limit] carregado")

    def health_check(self):
        return {"status": "healthy", "plugin": "rate_limit", "total": len(_tentativas)}

plugin = RateLimitPlugin()
