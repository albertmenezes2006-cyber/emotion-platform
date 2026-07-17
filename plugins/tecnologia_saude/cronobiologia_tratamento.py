#!/usr/bin/env python3
"""Cronobiologia no tratamento"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/crono-trat", tags=["Tecnologia Saude"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "cronobiologia_tratamento", "status": "ativo",
                          "descricao": "Cronobiologia no tratamento",
                          "categoria": "tecnologia_saude",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "cronobiologia_tratamento",
                          "descricao": "Cronobiologia no tratamento",
                          "categoria": "tecnologia_saude",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "cronobiologia_tratamento"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
