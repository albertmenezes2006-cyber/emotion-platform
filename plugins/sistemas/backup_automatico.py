#!/usr/bin/env python3
"""Backup automático"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/backup-auto", tags=["backup_auto"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "backup_auto", "status": "ativo",
                          "descricao": "Backup automático",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "backup_auto"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
