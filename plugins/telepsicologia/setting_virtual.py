#!/usr/bin/env python3
"""Setting terapêutico virtual"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/setting-virtual", tags=["Telepsicologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "setting_virtual", "status": "ativo",
                          "descricao": "Setting terapêutico virtual",
                          "versao": "1.0.0",
                          "categoria": "telepsicologia",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "setting_virtual"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
