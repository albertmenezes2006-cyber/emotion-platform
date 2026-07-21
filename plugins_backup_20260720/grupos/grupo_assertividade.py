#!/usr/bin/env python3
"""Grupo assertividade"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/grupo-assert", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "grupo_assertividade", "status": "ativo",
                          "descricao": "Grupo assertividade",
                          "categoria": "grupos",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "grupo_assertividade",
                          "descricao": "Grupo assertividade",
                          "categoria": "grupos",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "grupo_assertividade"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
