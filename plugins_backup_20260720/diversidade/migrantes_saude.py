#!/usr/bin/env python3
"""Saúde mental de migrantes"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/migrantes", tags=["Diversidade"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "migrantes_mental", "status": "ativo",
                          "descricao": "Saúde mental de migrantes",
                          "versao": "1.0.0",
                          "categoria": "diversidade",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "migrantes_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
