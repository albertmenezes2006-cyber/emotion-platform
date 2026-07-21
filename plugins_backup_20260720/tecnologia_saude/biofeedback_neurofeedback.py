#!/usr/bin/env python3
"""Biofeedback e neurofeedback"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/bio-neuro", tags=["Tecnologia Saude"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "biofeedback_neurofeedback", "status": "ativo",
                          "descricao": "Biofeedback e neurofeedback",
                          "categoria": "tecnologia_saude",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "biofeedback_neurofeedback",
                          "descricao": "Biofeedback e neurofeedback",
                          "categoria": "tecnologia_saude",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "biofeedback_neurofeedback"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
