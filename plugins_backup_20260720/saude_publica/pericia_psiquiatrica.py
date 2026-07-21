#!/usr/bin/env python3
"""Perícia psiquiátrica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/pericia-psiq", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "pericia_psiquiatrica", "status": "ativo",
                          "descricao": "Perícia psiquiátrica",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "pericia_psiquiatrica",
                          "descricao": "Perícia psiquiátrica",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "pericia_psiquiatrica"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
