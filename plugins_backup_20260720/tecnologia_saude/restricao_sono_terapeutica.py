#!/usr/bin/env python3
"""Restrição de sono terapêutica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/restricao-sono", tags=["Tecnologia Saude"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "restricao_sono_terapeutica", "status": "ativo",
                          "descricao": "Restrição de sono terapêutica",
                          "categoria": "tecnologia_saude",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "restricao_sono_terapeutica",
                          "descricao": "Restrição de sono terapêutica",
                          "categoria": "tecnologia_saude",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "restricao_sono_terapeutica"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
