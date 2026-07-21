#!/usr/bin/env python3
"""Chat especializado em CBT"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/chat-cbt", tags=["Ia Avancada"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "chat_cbt_ia", "status": "ativo",
                          "descricao": "Chat especializado em CBT",
                          "versao": "1.0.0",
                          "categoria": "ia_avancada",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "chat_cbt_ia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
