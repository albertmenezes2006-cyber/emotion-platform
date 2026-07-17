#!/usr/bin/env python3
"""Forest bathing evidências"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/forest-ev", tags=["Tecnologia Saude"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "forest_bathing_ev", "status": "ativo",
                          "descricao": "Forest bathing evidências",
                          "categoria": "tecnologia_saude",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "forest_bathing_ev",
                          "descricao": "Forest bathing evidências",
                          "categoria": "tecnologia_saude",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "forest_bathing_ev"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
