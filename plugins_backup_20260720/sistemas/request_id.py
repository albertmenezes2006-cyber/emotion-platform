#!/usr/bin/env python3
"""Middleware de Request ID"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/request-id", tags=["request_id_middleware"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "request_id_middleware", "status": "ativo",
                          "descricao": "Middleware de Request ID",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "request_id_middleware"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
