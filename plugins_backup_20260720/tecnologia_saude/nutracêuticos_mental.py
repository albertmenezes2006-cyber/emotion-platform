#!/usr/bin/env python3
"""Nutracêuticos em saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/nutraceuticos", tags=["Tecnologia Saude"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "nutracêuticos_mental", "status": "ativo",
                          "descricao": "Nutracêuticos em saúde mental",
                          "categoria": "tecnologia_saude",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "nutracêuticos_mental",
                          "descricao": "Nutracêuticos em saúde mental",
                          "categoria": "tecnologia_saude",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "nutracêuticos_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
