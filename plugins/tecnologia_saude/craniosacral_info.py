#!/usr/bin/env python3
"""Terapia craniosacral info"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/craniosacral", tags=["Tecnologia Saude"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "craniosacral_info", "status": "ativo",
                          "descricao": "Terapia craniosacral info",
                          "categoria": "tecnologia_saude",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "craniosacral_info",
                          "descricao": "Terapia craniosacral info",
                          "categoria": "tecnologia_saude",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "craniosacral_info"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
