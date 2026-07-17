#!/usr/bin/env python3
"""Well-being Therapy Fava"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/wbt", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "wellbeing_therapy", "status": "ativo",
                          "descricao": "Well-being Therapy Fava",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "wellbeing_therapy",
                          "descricao": "Well-being Therapy Fava",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "wellbeing_therapy"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
