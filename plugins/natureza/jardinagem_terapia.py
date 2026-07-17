#!/usr/bin/env python3
"""Jardinagem terapêutica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/jardinagem", tags=["Natureza"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "jardinagem_terapia", "status": "ativo",
                          "descricao": "Jardinagem terapêutica",
                          "versao": "1.0.0",
                          "categoria": "natureza",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "jardinagem_terapia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
