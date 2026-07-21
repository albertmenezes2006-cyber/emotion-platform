#!/usr/bin/env python3
"""Escrita expressiva Pennebaker"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/escrita", tags=["Arte Terapia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "escrita_expressiva", "status": "ativo",
                          "descricao": "Escrita expressiva Pennebaker",
                          "versao": "1.0.0",
                          "categoria": "arte_terapia",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "escrita_expressiva"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
