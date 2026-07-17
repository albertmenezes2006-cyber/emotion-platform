#!/usr/bin/env python3
"""Hipnoterapia clínica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/hipnoterapia", tags=["Tecnologia Saude"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "hipnoterapia_clinica", "status": "ativo",
                          "descricao": "Hipnoterapia clínica",
                          "categoria": "tecnologia_saude",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "hipnoterapia_clinica",
                          "descricao": "Hipnoterapia clínica",
                          "categoria": "tecnologia_saude",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "hipnoterapia_clinica"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
