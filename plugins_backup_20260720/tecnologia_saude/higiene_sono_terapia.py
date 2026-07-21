#!/usr/bin/env python3
"""Higiene do sono como terapia"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/sono-terapia", tags=["Tecnologia Saude"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "higiene_sono_terapia", "status": "ativo",
                          "descricao": "Higiene do sono como terapia",
                          "categoria": "tecnologia_saude",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "higiene_sono_terapia",
                          "descricao": "Higiene do sono como terapia",
                          "categoria": "tecnologia_saude",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "higiene_sono_terapia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
