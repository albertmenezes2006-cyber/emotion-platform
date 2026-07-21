#!/usr/bin/env python3
"""Validação de email"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/email-validar", tags=["validador_email"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "validador_email", "status": "ativo",
                          "descricao": "Validação de email",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "validador_email"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
