#!/usr/bin/env python3
"""Grupo MBSR 8 semanas"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/grupo-mindful-8", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "grupo_mindfulness_8sem", "status": "ativo",
                          "descricao": "Grupo MBSR 8 semanas",
                          "categoria": "grupos",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "grupo_mindfulness_8sem",
                          "descricao": "Grupo MBSR 8 semanas",
                          "categoria": "grupos",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "grupo_mindfulness_8sem"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
