#!/usr/bin/env python3
"""Empathic Listening"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/empathic_listening", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_empathic_listening","s":"ativo","d":"Empathic Listening","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_empathic_listening"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
