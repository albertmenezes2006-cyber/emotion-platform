#!/usr/bin/env python3
"""Systemic Individual"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/systemic_individual", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_systemic_individual","s":"ativo","d":"Systemic Individual","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_systemic_individual"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
