#!/usr/bin/env python3
"""Grupo profissionais de saúde"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/grupo-prof-saude", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "grupo_profissionais_saude", "status": "ativo",
                          "descricao": "Grupo profissionais de saúde",
                          "categoria": "grupos",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "grupo_profissionais_saude",
                          "descricao": "Grupo profissionais de saúde",
                          "categoria": "grupos",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "grupo_profissionais_saude"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
