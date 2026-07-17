#!/usr/bin/env python3
"""Programa bem-estar positivo"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/programa-pp", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "programa_bem_estar_pos", "status": "ativo",
                          "descricao": "Programa bem-estar positivo",
                          "categoria": "grupos",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "programa_bem_estar_pos",
                          "descricao": "Programa bem-estar positivo",
                          "categoria": "grupos",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "programa_bem_estar_pos"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
