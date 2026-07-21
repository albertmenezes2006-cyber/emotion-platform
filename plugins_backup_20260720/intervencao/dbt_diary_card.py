#!/usr/bin/env python3
"""DBT diary card digital"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/dbt-diary", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "dbt_diary_card", "status": "ativo",
                          "descricao": "DBT diary card digital",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "dbt_diary_card",
                          "descricao": "DBT diary card digital",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "dbt_diary_card"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
