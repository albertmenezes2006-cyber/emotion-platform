#!/usr/bin/env python3
"""Etapas do luto Kübler-Ross"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/luto-etapas", tags=["Luto"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "etapas_luto", "status": "ativo",
                          "descricao": "Etapas do luto Kübler-Ross",
                          "versao": "1.0.0",
                          "categoria": "luto",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "etapas_luto"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
