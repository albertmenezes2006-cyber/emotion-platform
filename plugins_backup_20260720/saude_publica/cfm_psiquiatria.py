#!/usr/bin/env python3
"""CFM e psiquiatria digital"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/cfm-psiq", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "cfm_psiquiatria", "status": "ativo",
                          "descricao": "CFM e psiquiatria digital",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "cfm_psiquiatria",
                          "descricao": "CFM e psiquiatria digital",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "cfm_psiquiatria"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
