#!/usr/bin/env python3
"""Grupo DBT completo"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/grupo-dbt", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "grupo_dbt_completo", "status": "ativo",
                          "descricao": "Grupo DBT completo",
                          "categoria": "grupos",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "grupo_dbt_completo",
                          "descricao": "Grupo DBT completo",
                          "categoria": "grupos",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "grupo_dbt_completo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
