#!/usr/bin/env python3
"""API versão 2 info"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v2", tags=["api_v2_info"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "api_v2_info", "status": "ativo",
                          "descricao": "API versão 2 info",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "api_v2_info"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
