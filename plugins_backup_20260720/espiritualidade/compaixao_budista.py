#!/usr/bin/env python3
"""Práticas de compaixão"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/compaixao", tags=["Espiritualidade"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "compaixao_budista", "status": "ativo",
                          "descricao": "Práticas de compaixão",
                          "versao": "1.0.0",
                          "categoria": "espiritualidade",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "compaixao_budista"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
