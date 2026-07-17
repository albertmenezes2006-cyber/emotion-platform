#!/usr/bin/env python3
"""ACT clarificação de valores"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/act-valores", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "act_values_clarif", "status": "ativo",
                          "descricao": "ACT clarificação de valores",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "act_values_clarif",
                          "descricao": "ACT clarificação de valores",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "act_values_clarif"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
