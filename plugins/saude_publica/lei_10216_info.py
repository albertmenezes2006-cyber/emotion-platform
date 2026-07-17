#!/usr/bin/env python3
"""Lei 10.216/2001 explicada"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/lei-10216", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "lei_10216_info", "status": "ativo",
                          "descricao": "Lei 10.216/2001 explicada",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "lei_10216_info",
                          "descricao": "Lei 10.216/2001 explicada",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "lei_10216_info"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
