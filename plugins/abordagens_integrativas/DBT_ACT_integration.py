#!/usr/bin/env python3
"""Dbt Act Integration"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/DBT_ACT_integration", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_DBT_ACT_integration","s":"ativo","d":"Dbt Act Integration","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_DBT_ACT_integration"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
