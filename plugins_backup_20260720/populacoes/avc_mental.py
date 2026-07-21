#!/usr/bin/env python3
"""AVC e saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/avc", tags=["Populacoes"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "avc_mental", "status": "ativo",
                          "descricao": "AVC e saúde mental",
                          "categoria": "populacoes",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "avc_mental",
                          "descricao": "AVC e saúde mental",
                          "categoria": "populacoes",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "avc_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
