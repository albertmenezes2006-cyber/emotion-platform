#!/usr/bin/env python3
"""DBT habilidades de crise"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/dbt-crisis", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "dbt_crisis_survival", "status": "ativo",
                          "descricao": "DBT habilidades de crise",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "dbt_crisis_survival",
                          "descricao": "DBT habilidades de crise",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "dbt_crisis_survival"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
