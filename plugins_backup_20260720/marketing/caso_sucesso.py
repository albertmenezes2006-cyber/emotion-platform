#!/usr/bin/env python3
"""Casos de sucesso"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/casos", tags=["caso_sucesso"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "caso_sucesso", "status": "ativo",
                          "descricao": "Casos de sucesso",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "caso_sucesso"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
