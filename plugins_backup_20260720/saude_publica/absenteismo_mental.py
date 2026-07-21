#!/usr/bin/env python3
"""Absenteísmo e saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/absenteismo-mental", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "absenteismo_mental", "status": "ativo",
                          "descricao": "Absenteísmo e saúde mental",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "absenteismo_mental",
                          "descricao": "Absenteísmo e saúde mental",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "absenteismo_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
