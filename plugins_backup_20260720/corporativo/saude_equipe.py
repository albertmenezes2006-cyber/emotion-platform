#!/usr/bin/env python3
"""Saúde mental de equipes"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/equipe", tags=["Corporativo"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "saude_equipe", "status": "ativo",
                          "descricao": "Saúde mental de equipes",
                          "versao": "1.0.0",
                          "categoria": "corporativo",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "saude_equipe"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
