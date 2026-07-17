#!/usr/bin/env python3
"""Grupos de apoio online"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/grupo-online", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "grupo_online_apoio", "status": "ativo",
                          "descricao": "Grupos de apoio online",
                          "categoria": "grupos",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "grupo_online_apoio",
                          "descricao": "Grupos de apoio online",
                          "categoria": "grupos",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "grupo_online_apoio"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
