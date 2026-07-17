#!/usr/bin/env python3
"""Ecoterapia e natureza"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/ecoterapia", tags=["Natureza"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "ecoterapia", "status": "ativo",
                          "descricao": "Ecoterapia e natureza",
                          "versao": "1.0.0",
                          "categoria": "natureza",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "ecoterapia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
