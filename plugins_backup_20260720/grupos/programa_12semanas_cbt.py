#!/usr/bin/env python3
"""Programa 12 semanas CBT"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/programa-12sem", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "programa_12semanas_cbt", "status": "ativo",
                          "descricao": "Programa 12 semanas CBT",
                          "categoria": "grupos",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "programa_12semanas_cbt",
                          "descricao": "Programa 12 semanas CBT",
                          "categoria": "grupos",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "programa_12semanas_cbt"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
