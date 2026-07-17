#!/usr/bin/env python3
"""Fototerapia e autoconhecimento"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/fotografia", tags=["Arte Terapia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "fotografia_terapia", "status": "ativo",
                          "descricao": "Fototerapia e autoconhecimento",
                          "versao": "1.0.0",
                          "categoria": "arte_terapia",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "fotografia_terapia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
