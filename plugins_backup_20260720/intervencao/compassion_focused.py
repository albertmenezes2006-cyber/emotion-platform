#!/usr/bin/env python3
"""CFT Compassion Focused Therapy"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/cft-protocol", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "compassion_focused", "status": "ativo",
                          "descricao": "CFT Compassion Focused Therapy",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "compassion_focused",
                          "descricao": "CFT Compassion Focused Therapy",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "compassion_focused"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
