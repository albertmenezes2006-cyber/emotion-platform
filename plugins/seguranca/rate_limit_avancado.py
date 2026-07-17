#!/usr/bin/env python3
"""Rate limiting avancado por IP"""
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from starlette.middleware.base import BaseHTTPMiddleware
from collections import defaultdict
from datetime import datetime, timedelta
import time

router = APIRouter(prefix="/api/v1/rate-limit", tags=["RateLimit"])

# Armazenamento em memória
_requests = defaultdict(list)
_blocked = {}

LIMITE_POR_MINUTO = 60
LIMITE_BURST = 100

class RateLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        ip = request.client.host if request.client else "unknown"
        agora = time.time()
        # Verificar bloqueio
        if ip in _blocked:
            if agora < _blocked[ip]:
                return JSONResponse(
                    {"erro": "Too many requests", "retry_after": 60},
                    status_code=429,
                    headers={"Retry-After": "60"}
                )
            else:
                del _blocked[ip]
        # Limpar requests antigas
        _requests[ip] = [t for t in _requests[ip] if agora - t < 60]
        # Verificar limite
        if len(_requests[ip]) >= LIMITE_BURST:
            _blocked[ip] = agora + 300  # bloquear 5 min
            return JSONResponse(
                {"erro": "Rate limit exceeded", "blocked_for": "5 minutes"},
                status_code=429
            )
        _requests[ip].append(agora)
        response = await call_next(request)
        response.headers["X-RateLimit-Limit"] = str(LIMITE_POR_MINUTO)
        response.headers["X-RateLimit-Remaining"] = str(
            max(0, LIMITE_POR_MINUTO - len(_requests[ip]))
        )
        return response

@router.get("/status")
async def rate_status(request: Request):
    ip = request.client.host if request.client else "unknown"
    agora = time.time()
    recentes = [t for t in _requests.get(ip, []) if agora - t < 60]
    return {
        "seu_ip": ip,
        "requests_ultimo_minuto": len(recentes),
        "limite": LIMITE_POR_MINUTO,
        "bloqueado": ip in _blocked
    }

class RateLimitPlugin(PluginBase):
    name = "rate_limit_avancado"
    def setup(self, app):
        app.add_middleware(RateLimitMiddleware)
        app.include_router(router)

plugin = RateLimitPlugin()
