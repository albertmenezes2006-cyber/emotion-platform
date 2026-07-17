#!/usr/bin/env python3
"""Circuit breaker"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/circuit", tags=["circuit_breaker"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "circuit_breaker", "status": "ativo",
                          "descricao": "Circuit breaker",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "circuit_breaker"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
