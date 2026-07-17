#!/usr/bin/env python3
"""EMDR estimulação bilateral"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/emdr-bilateral", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "emdr_bilateral", "status": "ativo",
                          "descricao": "EMDR estimulação bilateral",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "emdr_bilateral",
                          "descricao": "EMDR estimulação bilateral",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "emdr_bilateral"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
