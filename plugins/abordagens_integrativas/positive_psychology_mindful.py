#!/usr/bin/env python3
"""Positive Psychology Mindful"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/positive_psychology_mindful", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_positive_psychology_mindf","s":"ativo","d":"Positive Psychology Mindful","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_positive_psychology_mindf"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
