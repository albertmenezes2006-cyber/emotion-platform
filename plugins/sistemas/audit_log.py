#!/usr/bin/env python3
"""Log de auditoria"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/audit", tags=["audit_log"])

@router.get("")
async def info():
    return JSONResponse({"nome": "audit_log", "status": "ativo",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "audit_log"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
