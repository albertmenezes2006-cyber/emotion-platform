#!/usr/bin/env python3
"""Polyvagal Informed"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/polyvagal_informed", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_polyvagal_informed","s":"ativo","d":"Polyvagal Informed","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_polyvagal_informed"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
