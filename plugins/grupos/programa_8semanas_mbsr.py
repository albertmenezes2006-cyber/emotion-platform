#!/usr/bin/env python3
"""Programa 8 semanas MBSR"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/programa-8sem", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "programa_8semanas_mbsr", "status": "ativo",
                          "descricao": "Programa 8 semanas MBSR",
                          "categoria": "grupos",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "programa_8semanas_mbsr",
                          "descricao": "Programa 8 semanas MBSR",
                          "categoria": "grupos",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "programa_8semanas_mbsr"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
