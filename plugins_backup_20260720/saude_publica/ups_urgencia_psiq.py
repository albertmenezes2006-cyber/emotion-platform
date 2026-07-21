#!/usr/bin/env python3
"""UPS urgência psiquiátrica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/ups", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "ups_urgencia_psiq", "status": "ativo",
                          "descricao": "UPS urgência psiquiátrica",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "ups_urgencia_psiq",
                          "descricao": "UPS urgência psiquiátrica",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "ups_urgencia_psiq"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
