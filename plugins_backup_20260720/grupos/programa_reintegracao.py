#!/usr/bin/env python3
"""Programa reintegração social"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/reintegracao", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "programa_reintegracao", "status": "ativo",
                          "descricao": "Programa reintegração social",
                          "categoria": "grupos",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "programa_reintegracao",
                          "descricao": "Programa reintegração social",
                          "categoria": "grupos",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "programa_reintegracao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
