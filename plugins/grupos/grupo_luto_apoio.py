#!/usr/bin/env python3
"""Grupo apoio ao luto"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/grupo-luto-ap", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "grupo_luto_apoio", "status": "ativo",
                          "descricao": "Grupo apoio ao luto",
                          "categoria": "grupos",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "grupo_luto_apoio",
                          "descricao": "Grupo apoio ao luto",
                          "categoria": "grupos",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "grupo_luto_apoio"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
