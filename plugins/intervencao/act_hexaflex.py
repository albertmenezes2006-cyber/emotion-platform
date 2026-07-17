#!/usr/bin/env python3
"""ACT hexaflex interativo"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/act-hexaflex", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "act_hexaflex", "status": "ativo",
                          "descricao": "ACT hexaflex interativo",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "act_hexaflex",
                          "descricao": "ACT hexaflex interativo",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "act_hexaflex"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
