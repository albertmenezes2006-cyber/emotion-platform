#!/usr/bin/env python3
"""Grupo de suporte ao trauma"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/grupo-trauma", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "grupo_trauma", "status": "ativo",
                          "descricao": "Grupo de suporte ao trauma",
                          "versao": "1.0.0",
                          "categoria": "grupos",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "grupo_trauma"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
