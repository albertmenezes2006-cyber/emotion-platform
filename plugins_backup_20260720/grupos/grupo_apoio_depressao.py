#!/usr/bin/env python3
"""Grupo de apoio à depressão"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/grupo-depressao", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "grupo_depressao", "status": "ativo",
                          "descricao": "Grupo de apoio à depressão",
                          "versao": "1.0.0",
                          "categoria": "grupos",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "grupo_depressao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
