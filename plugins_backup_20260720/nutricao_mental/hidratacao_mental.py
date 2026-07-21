#!/usr/bin/env python3
"""Hidratação e cognição"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/hidratacao", tags=["Nutricao Mental"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "hidratacao_mental", "status": "ativo",
                          "descricao": "Hidratação e cognição",
                          "versao": "1.0.0",
                          "categoria": "nutricao_mental",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "hidratacao_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
