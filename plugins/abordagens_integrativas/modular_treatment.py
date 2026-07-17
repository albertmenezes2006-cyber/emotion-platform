#!/usr/bin/env python3
"""Modular Treatment"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/modular_treatment", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_modular_treatment","s":"ativo","d":"Modular Treatment","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_modular_treatment"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
