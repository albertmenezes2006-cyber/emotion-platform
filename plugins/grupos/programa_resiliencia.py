#!/usr/bin/env python3
"""Programa construção resiliência"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/programa-resil", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "programa_resiliencia", "status": "ativo",
                          "descricao": "Programa construção resiliência",
                          "categoria": "grupos",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "programa_resiliencia",
                          "descricao": "Programa construção resiliência",
                          "categoria": "grupos",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "programa_resiliencia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
