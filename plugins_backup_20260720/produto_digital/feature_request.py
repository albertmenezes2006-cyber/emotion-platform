#!/usr/bin/env python3
"""Sistema de solicitacao de features"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/feature-request", tags=["Essencial"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "feature_request", "status": "ativo",
                          "descricao": "Sistema de solicitacao de features",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "feature_request"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
