#!/usr/bin/env python3
"""Schema Focused Integrative"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/schema_focused_integrative", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_schema_focused_integrativ","s":"ativo","d":"Schema Focused Integrative","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_schema_focused_integrativ"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
