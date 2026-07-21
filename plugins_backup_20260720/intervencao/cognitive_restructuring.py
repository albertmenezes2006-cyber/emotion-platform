#!/usr/bin/env python3
"""Reestruturação cognitiva"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/reestruturacao", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "cognitive_restructuring", "status": "ativo",
                          "descricao": "Reestruturação cognitiva",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "cognitive_restructuring",
                          "descricao": "Reestruturação cognitiva",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "cognitive_restructuring"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
