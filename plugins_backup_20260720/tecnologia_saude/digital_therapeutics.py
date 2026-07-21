#!/usr/bin/env python3
"""Digital Therapeutics DTx"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/dtx", tags=["Tecnologia Saude"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "digital_therapeutics_info", "status": "ativo",
                          "descricao": "Digital Therapeutics DTx",
                          "versao": "1.0.0",
                          "categoria": "tecnologia_saude",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "digital_therapeutics_info"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
