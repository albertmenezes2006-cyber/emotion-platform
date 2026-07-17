#!/usr/bin/env python3
"""Padrões mHealth"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/mhealth", tags=["Tecnologia Saude"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "mhealth_std", "status": "ativo",
                          "descricao": "Padrões mHealth",
                          "versao": "1.0.0",
                          "categoria": "tecnologia_saude",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "mhealth_std"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
