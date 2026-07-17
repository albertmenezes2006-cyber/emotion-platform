#!/usr/bin/env python3
"""Comunicação com equipe de saúde"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/com-equipe", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "comunicacao_equipe_saude", "status": "ativo",
                          "descricao": "Comunicação com equipe de saúde",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "comunicacao_equipe_saude",
                          "descricao": "Comunicação com equipe de saúde",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "comunicacao_equipe_saude"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
