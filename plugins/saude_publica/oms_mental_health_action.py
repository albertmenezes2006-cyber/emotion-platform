#!/usr/bin/env python3
"""OMS Plano Ação Saúde Mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/oms-action", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "oms_mental_health_action", "status": "ativo",
                          "descricao": "OMS Plano Ação Saúde Mental",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "oms_mental_health_action",
                          "descricao": "OMS Plano Ação Saúde Mental",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "oms_mental_health_action"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
