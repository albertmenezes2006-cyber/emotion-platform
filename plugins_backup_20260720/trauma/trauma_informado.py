#!/usr/bin/env python3
"""Cuidado informado pelo trauma"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/trauma-care", tags=["Trauma"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "care_trauma_info", "status": "ativo",
                          "descricao": "Cuidado informado pelo trauma",
                          "versao": "1.0.0",
                          "categoria": "trauma",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "care_trauma_info"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
