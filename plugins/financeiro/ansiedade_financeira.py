#!/usr/bin/env python3
"""Suporte à ansiedade financeira"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/ansiedade-financeira", tags=["Financeiro"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "ansiedade_fin", "status": "ativo",
                          "descricao": "Suporte à ansiedade financeira",
                          "versao": "1.0.0",
                          "categoria": "financeiro",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "ansiedade_fin"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
