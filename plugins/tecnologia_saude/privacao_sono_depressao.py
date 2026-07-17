#!/usr/bin/env python3
"""Privação de sono em depressão"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/privacao-sono", tags=["Tecnologia Saude"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "privacao_sono_depressao", "status": "ativo",
                          "descricao": "Privação de sono em depressão",
                          "categoria": "tecnologia_saude",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "privacao_sono_depressao",
                          "descricao": "Privação de sono em depressão",
                          "categoria": "tecnologia_saude",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "privacao_sono_depressao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
