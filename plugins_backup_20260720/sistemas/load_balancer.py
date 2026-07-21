#!/usr/bin/env python3
"""Info de carga do sistema"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/load", tags=["load_info"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "load_info", "status": "ativo",
                          "descricao": "Info de carga do sistema",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "load_info"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
