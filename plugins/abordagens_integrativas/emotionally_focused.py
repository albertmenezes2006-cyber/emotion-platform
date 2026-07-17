#!/usr/bin/env python3
"""Emotionally Focused"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/emotionally_focused", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_emotionally_focused","s":"ativo","d":"Emotionally Focused","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_emotionally_focused"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
