#!/usr/bin/env python3
"""Sympathetic Joy"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/sympathetic_joy", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_sympathetic_joy","s":"ativo","d":"Sympathetic Joy","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_sympathetic_joy"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
