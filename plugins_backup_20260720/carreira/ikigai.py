#!/usr/bin/env python3
"""Ferramenta Ikigai interativa"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/ikigai", tags=["Carreira"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "ikigai_tool", "status": "ativo",
                          "descricao": "Ferramenta Ikigai interativa",
                          "versao": "1.0.0",
                          "categoria": "carreira",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "ikigai_tool"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
