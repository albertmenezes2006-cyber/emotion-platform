#!/usr/bin/env python3
"""Atitude Mudanca"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/atitude_mudanca", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__atitude_mudanca","s":"ativo","d":"Atitude Mudanca","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__atitude_mudanca"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
