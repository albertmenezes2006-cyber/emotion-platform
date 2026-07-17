#!/usr/bin/env python3
"""Culturally Adapted"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/culturally_adapted", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_culturally_adapted","s":"ativo","d":"Culturally Adapted","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_culturally_adapted"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
