#!/usr/bin/env python3
"""Metacognitive Training psicose"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/mct-psicose", tags=["Neuropsicologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "metacog_training_psicose", "status": "ativo",
                          "descricao": "Metacognitive Training psicose",
                          "categoria": "neuropsicologia",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "metacog_training_psicose",
                          "descricao": "Metacognitive Training psicose",
                          "categoria": "neuropsicologia",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "metacog_training_psicose"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
