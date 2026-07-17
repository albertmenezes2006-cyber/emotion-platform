#!/usr/bin/env python3
"""TMS estimulação magnética info"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/tms", tags=["Tecnologia Saude"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "TMS_info", "status": "ativo",
                          "descricao": "TMS estimulação magnética info",
                          "categoria": "tecnologia_saude",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "TMS_info",
                          "descricao": "TMS estimulação magnética info",
                          "categoria": "tecnologia_saude",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "TMS_info"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
