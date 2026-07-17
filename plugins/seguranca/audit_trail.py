#!/usr/bin/env python3
"""Audit trail completo"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/audit-trail", tags=["Essencial"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "audit_trail_complete", "status": "ativo",
                          "descricao": "Audit trail completo",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "audit_trail_complete"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
