#!/usr/bin/env python3
"""Grounding com a terra"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/grounding-terra", tags=["Tecnologia Saude"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "terra_grounding", "status": "ativo",
                          "descricao": "Grounding com a terra",
                          "categoria": "tecnologia_saude",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "terra_grounding",
                          "descricao": "Grounding com a terra",
                          "categoria": "tecnologia_saude",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "terra_grounding"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
