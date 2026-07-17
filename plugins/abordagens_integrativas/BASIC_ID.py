#!/usr/bin/env python3
"""Basic Id"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/BASIC_ID", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_BASIC_ID","s":"ativo","d":"Basic Id","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_BASIC_ID"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
