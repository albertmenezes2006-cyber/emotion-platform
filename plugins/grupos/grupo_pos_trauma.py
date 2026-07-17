#!/usr/bin/env python3
"""Grupo pós-trauma"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/grupo-pos-trauma", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "grupo_pos_trauma", "status": "ativo",
                          "descricao": "Grupo pós-trauma",
                          "categoria": "grupos",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "grupo_pos_trauma",
                          "descricao": "Grupo pós-trauma",
                          "categoria": "grupos",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "grupo_pos_trauma"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
