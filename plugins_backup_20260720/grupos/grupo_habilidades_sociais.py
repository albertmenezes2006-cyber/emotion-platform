#!/usr/bin/env python3
"""Grupo habilidades sociais"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/grupo-hs", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "grupo_habilidades_sociais", "status": "ativo",
                          "descricao": "Grupo habilidades sociais",
                          "categoria": "grupos",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "grupo_habilidades_sociais",
                          "descricao": "Grupo habilidades sociais",
                          "categoria": "grupos",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "grupo_habilidades_sociais"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
