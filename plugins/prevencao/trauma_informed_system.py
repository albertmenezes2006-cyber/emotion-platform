#!/usr/bin/env python3
"""Sistema informado pelo trauma"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/sistema-trauma", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "trauma_informed_system", "status": "ativo",
                          "descricao": "Sistema informado pelo trauma",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "trauma_informed_system",
                          "descricao": "Sistema informado pelo trauma",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "trauma_informed_system"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
