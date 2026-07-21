#!/usr/bin/env python3
"""Saúde mental de professores"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/professores", tags=["Escola"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "prof_saude", "status": "ativo",
                          "descricao": "Saúde mental de professores",
                          "versao": "1.0.0",
                          "categoria": "escola",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "prof_saude"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
