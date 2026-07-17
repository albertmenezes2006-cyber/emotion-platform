#!/usr/bin/env python3
"""Developmental Couple"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/developmental_couple", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_developmental_couple","s":"ativo","d":"Developmental Couple","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_developmental_couple"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
