#!/usr/bin/env python3
"""Customer success digital"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/cs", tags=["Marketing"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "customer_success", "status": "ativo",
                          "descricao": "Customer success digital",
                          "versao": "1.0.0",
                          "categoria": "marketing",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "customer_success"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
