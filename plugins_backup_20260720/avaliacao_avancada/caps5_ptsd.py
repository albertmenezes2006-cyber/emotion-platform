#!/usr/bin/env python3
"""CAPS-5 PTSD clínico"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/caps5", tags=["Avaliacao Avancada"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "caps5_ptsd", "status": "ativo",
                          "descricao": "CAPS-5 PTSD clínico",
                          "categoria": "avaliacao_avancada",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "caps5_ptsd",
                          "descricao": "CAPS-5 PTSD clínico",
                          "categoria": "avaliacao_avancada",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "caps5_ptsd"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
