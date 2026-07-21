#!/usr/bin/env python3
"""Acupuntura e saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/acupuntura-mental", tags=["Tecnologia Saude"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "acupuntura_mental_info", "status": "ativo",
                          "descricao": "Acupuntura e saúde mental",
                          "categoria": "tecnologia_saude",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "acupuntura_mental_info",
                          "descricao": "Acupuntura e saúde mental",
                          "categoria": "tecnologia_saude",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "acupuntura_mental_info"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
