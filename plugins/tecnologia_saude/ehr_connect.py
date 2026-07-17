#!/usr/bin/env python3
"""Conexão com prontuários"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/ehr", tags=["Tecnologia Saude"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "ehr_connect", "status": "ativo",
                          "descricao": "Conexão com prontuários",
                          "versao": "1.0.0",
                          "categoria": "tecnologia_saude",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "ehr_connect"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
