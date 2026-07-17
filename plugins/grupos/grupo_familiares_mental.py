#!/usr/bin/env python3
"""Grupo familiares saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/grupo-familiares", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "grupo_familiares_mental", "status": "ativo",
                          "descricao": "Grupo familiares saúde mental",
                          "categoria": "grupos",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "grupo_familiares_mental",
                          "descricao": "Grupo familiares saúde mental",
                          "categoria": "grupos",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "grupo_familiares_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
