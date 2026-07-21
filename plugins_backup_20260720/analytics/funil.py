#!/usr/bin/env python3
"""Funil de conversão"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/funil", tags=["funil_conversao"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "funil_conversao", "status": "ativo",
                          "descricao": "Funil de conversão",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "funil_conversao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
