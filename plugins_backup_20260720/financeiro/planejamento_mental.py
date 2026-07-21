#!/usr/bin/env python3
"""Saúde mental no planejamento financeiro"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/plan-fin", tags=["Financeiro"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "planejamento_mental_fin", "status": "ativo",
                          "descricao": "Saúde mental no planejamento financeiro",
                          "versao": "1.0.0",
                          "categoria": "financeiro",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "planejamento_mental_fin"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
