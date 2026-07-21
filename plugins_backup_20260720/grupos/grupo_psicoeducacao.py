#!/usr/bin/env python3
"""Grupo psicoeducação"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/grupo-psicoed", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "grupo_psicoeducacao", "status": "ativo",
                          "descricao": "Grupo psicoeducação",
                          "categoria": "grupos",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "grupo_psicoeducacao",
                          "descricao": "Grupo psicoeducação",
                          "categoria": "grupos",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "grupo_psicoeducacao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
