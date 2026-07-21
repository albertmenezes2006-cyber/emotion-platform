#!/usr/bin/env python3
"""Psicoeducação PTSD"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/psicoed-ptsd", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "psicoeducacao_ptsd", "status": "ativo",
                          "descricao": "Psicoeducação PTSD",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "psicoeducacao_ptsd",
                          "descricao": "Psicoeducação PTSD",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "psicoeducacao_ptsd"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
