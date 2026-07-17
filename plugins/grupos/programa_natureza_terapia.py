#!/usr/bin/env python3
"""Programa natureza e saúde"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/natureza-prog", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "programa_natureza_terapia", "status": "ativo",
                          "descricao": "Programa natureza e saúde",
                          "categoria": "grupos",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "programa_natureza_terapia",
                          "descricao": "Programa natureza e saúde",
                          "categoria": "grupos",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "programa_natureza_terapia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
