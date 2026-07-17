#!/usr/bin/env python3
"""Escrita expressiva para trauma"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/escrita-trauma", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "trauma_writing_protocol", "status": "ativo",
                          "descricao": "Escrita expressiva para trauma",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "trauma_writing_protocol",
                          "descricao": "Escrita expressiva para trauma",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "trauma_writing_protocol"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
