#!/usr/bin/env python3
"""Utilitários de números"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/numeros", tags=["numero_utils"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "numero_utils", "status": "ativo",
                          "descricao": "Utilitários de números",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "numero_utils"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
