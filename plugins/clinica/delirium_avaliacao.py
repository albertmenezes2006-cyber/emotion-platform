#!/usr/bin/env python3
"""Avaliação de delirium"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/delirium", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "delirium_avaliacao", "status": "ativo",
                          "descricao": "Avaliação de delirium",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "delirium_avaliacao",
                          "descricao": "Avaliação de delirium",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "delirium_avaliacao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
