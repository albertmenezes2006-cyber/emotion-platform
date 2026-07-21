#!/usr/bin/env python3
"""ACT ação comprometida"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/act-acao", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "act_committed_action", "status": "ativo",
                          "descricao": "ACT ação comprometida",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "act_committed_action",
                          "descricao": "ACT ação comprometida",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "act_committed_action"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
