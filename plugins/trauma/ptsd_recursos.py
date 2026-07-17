#!/usr/bin/env python3
"""Recursos para PTSD"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/ptsd", tags=["Trauma"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "ptsd_recursos", "status": "ativo",
                          "descricao": "Recursos para PTSD",
                          "versao": "1.0.0",
                          "categoria": "trauma",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "ptsd_recursos"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
