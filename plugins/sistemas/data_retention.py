#!/usr/bin/env python3
"""Política de retenção de dados"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/retention", tags=["Sistemas"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "data_retention", "status": "ativo",
                          "descricao": "Política de retenção de dados",
                          "versao": "1.0.0",
                          "categoria": "sistemas",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "data_retention"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
