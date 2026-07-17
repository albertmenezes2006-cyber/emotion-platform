#!/usr/bin/env python3
"""Tsc1 Tsc2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/tsc1_tsc2", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_tsc1_tsc2","s":"ativo","d":"Tsc1 Tsc2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_tsc1_tsc2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
