#!/usr/bin/env python3
"""Schema Emdr"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/schema_EMDR", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_schema_EMDR","s":"ativo","d":"Schema Emdr","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_schema_EMDR"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
