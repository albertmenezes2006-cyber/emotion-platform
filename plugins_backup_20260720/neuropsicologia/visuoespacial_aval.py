#!/usr/bin/env python3
"""Habilidades visuoespaciais"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/visuoespacial", tags=["Neuropsicologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "visuoespacial_aval", "status": "ativo",
                          "descricao": "Habilidades visuoespaciais",
                          "categoria": "neuropsicologia",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "visuoespacial_aval",
                          "descricao": "Habilidades visuoespaciais",
                          "categoria": "neuropsicologia",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "visuoespacial_aval"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
