#!/usr/bin/env python3
"""Lúpus e saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/lupus", tags=["Populacoes"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "lupus_mental", "status": "ativo",
                          "descricao": "Lúpus e saúde mental",
                          "categoria": "populacoes",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "lupus_mental",
                          "descricao": "Lúpus e saúde mental",
                          "categoria": "populacoes",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "lupus_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
