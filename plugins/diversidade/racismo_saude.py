#!/usr/bin/env python3
"""Racismo e saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/racismo-saude", tags=["Diversidade"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "racismo_saude_mental", "status": "ativo",
                          "descricao": "Racismo e saúde mental",
                          "versao": "1.0.0",
                          "categoria": "diversidade",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "racismo_saude_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
