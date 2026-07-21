#!/usr/bin/env python3
"""Redes sociais e bem-estar"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/redes-bem-estar", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "social_media_wellbeing", "status": "ativo",
                          "descricao": "Redes sociais e bem-estar",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "social_media_wellbeing",
                          "descricao": "Redes sociais e bem-estar",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "social_media_wellbeing"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
