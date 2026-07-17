#!/usr/bin/env python3
"""Multidimensional Family"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/multidimensional_family", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_multidimensional_family","s":"ativo","d":"Multidimensional Family","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_multidimensional_family"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
