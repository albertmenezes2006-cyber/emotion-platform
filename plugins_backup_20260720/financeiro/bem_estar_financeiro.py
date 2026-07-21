#!/usr/bin/env python3
"""Bem-estar financeiro e saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/bem-estar-fin", tags=["Financeiro"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "bem_estar_fin", "status": "ativo",
                          "descricao": "Bem-estar financeiro e saúde mental",
                          "versao": "1.0.0",
                          "categoria": "financeiro",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "bem_estar_fin"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
