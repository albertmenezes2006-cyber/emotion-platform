#!/usr/bin/env python3
"""Mindfulness Act"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/mindfulness_ACT", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_mindfulness_ACT","s":"ativo","d":"Mindfulness Act","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_mindfulness_ACT"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
