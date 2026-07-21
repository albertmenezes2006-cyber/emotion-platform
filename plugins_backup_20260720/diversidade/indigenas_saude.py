#!/usr/bin/env python3
"""Saúde mental indígena"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/indigenas", tags=["Diversidade"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "indigenas_mental", "status": "ativo",
                          "descricao": "Saúde mental indígena",
                          "versao": "1.0.0",
                          "categoria": "diversidade",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "indigenas_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
