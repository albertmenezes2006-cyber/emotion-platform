#!/usr/bin/env python3
"""Fototerapia para SAD"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/luz-terapia", tags=["Tecnologia Saude"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "luz_terapia_sad", "status": "ativo",
                          "descricao": "Fototerapia para SAD",
                          "categoria": "tecnologia_saude",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "luz_terapia_sad",
                          "descricao": "Fototerapia para SAD",
                          "categoria": "tecnologia_saude",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "luz_terapia_sad"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
