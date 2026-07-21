#!/usr/bin/env python3
"""Grupo universitários saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/grupo-univ", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "grupo_universitarios_sm", "status": "ativo",
                          "descricao": "Grupo universitários saúde mental",
                          "categoria": "grupos",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "grupo_universitarios_sm",
                          "descricao": "Grupo universitários saúde mental",
                          "categoria": "grupos",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "grupo_universitarios_sm"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
