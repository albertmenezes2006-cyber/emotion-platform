#!/usr/bin/env python3
"""Saúde mental na aposentadoria"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/aposentadoria", tags=["Gerontologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "aposentadoria_mental", "status": "ativo",
                          "descricao": "Saúde mental na aposentadoria",
                          "versao": "1.0.0",
                          "categoria": "gerontologia",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "aposentadoria_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
