#!/usr/bin/env python3
"""Mental Health First Aid"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/mhfa", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "mental_health_first_aid", "status": "ativo",
                          "descricao": "Mental Health First Aid",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "mental_health_first_aid",
                          "descricao": "Mental Health First Aid",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "mental_health_first_aid"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
