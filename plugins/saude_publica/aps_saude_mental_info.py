#!/usr/bin/env python3
"""APS e saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/aps-mental", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "aps_saude_mental_info", "status": "ativo",
                          "descricao": "APS e saúde mental",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "aps_saude_mental_info",
                          "descricao": "APS e saúde mental",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "aps_saude_mental_info"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
