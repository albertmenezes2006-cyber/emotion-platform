#!/usr/bin/env python3
"""Psychodynamic Cbt Integration"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/psychodynamic_cbt_integratio", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_psychodynamic_cbt_integra","s":"ativo","d":"Psychodynamic Cbt Integration","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_psychodynamic_cbt_integra"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
