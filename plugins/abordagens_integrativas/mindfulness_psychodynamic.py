#!/usr/bin/env python3
"""Mindfulness Psychodynamic"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/mindfulness_psychodynamic", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_mindfulness_psychodynamic","s":"ativo","d":"Mindfulness Psychodynamic","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_mindfulness_psychodynamic"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
