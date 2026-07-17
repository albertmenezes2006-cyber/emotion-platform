#!/usr/bin/env python3
"""Positive Psychology Dbt"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/positive_psychology_DBT", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_positive_psychology_DBT","s":"ativo","d":"Positive Psychology Dbt","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_positive_psychology_DBT"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
