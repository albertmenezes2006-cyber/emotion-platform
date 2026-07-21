#!/usr/bin/env python3
"""Programa qigong e saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/qigong", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "programa_qigong", "status": "ativo",
                          "descricao": "Programa qigong e saúde mental",
                          "categoria": "grupos",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "programa_qigong",
                          "descricao": "Programa qigong e saúde mental",
                          "categoria": "grupos",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "programa_qigong"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
