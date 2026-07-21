#!/usr/bin/env python3
"""NET Narrative Exposure Therapy"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/net", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "net_narrative_trauma", "status": "ativo",
                          "descricao": "NET Narrative Exposure Therapy",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "net_narrative_trauma",
                          "descricao": "NET Narrative Exposure Therapy",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "net_narrative_trauma"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
