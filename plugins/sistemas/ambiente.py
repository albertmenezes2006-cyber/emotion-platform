#!/usr/bin/env python3
"""Info do ambiente de execução"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/ambiente", tags=["ambiente_info"])

@router.get("")
async def info():
    return JSONResponse({"nome": "ambiente_info", "status": "ativo",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "ambiente_info"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
