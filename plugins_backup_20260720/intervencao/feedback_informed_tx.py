#!/usr/bin/env python3
"""FIT feedback informed treatment"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/fit-protocol", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "feedback_informed_tx", "status": "ativo",
                          "descricao": "FIT feedback informed treatment",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "feedback_informed_tx",
                          "descricao": "FIT feedback informed treatment",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "feedback_informed_tx"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
