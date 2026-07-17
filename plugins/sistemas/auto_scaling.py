#!/usr/bin/env python3
"""Auto scaling info"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/scaling", tags=["Sistemas"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "auto_scaling", "status": "ativo",
                          "descricao": "Auto scaling info",
                          "versao": "1.0.0",
                          "categoria": "sistemas",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "auto_scaling"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
