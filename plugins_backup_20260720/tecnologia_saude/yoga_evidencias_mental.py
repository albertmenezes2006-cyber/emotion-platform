#!/usr/bin/env python3
"""Yoga e saúde mental evidências"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/yoga-ev", tags=["Tecnologia Saude"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "yoga_evidencias_mental", "status": "ativo",
                          "descricao": "Yoga e saúde mental evidências",
                          "categoria": "tecnologia_saude",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "yoga_evidencias_mental",
                          "descricao": "Yoga e saúde mental evidências",
                          "categoria": "tecnologia_saude",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "yoga_evidencias_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
