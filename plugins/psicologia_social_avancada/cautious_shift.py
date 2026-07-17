#!/usr/bin/env python3
"""Cautious Shift"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/cautious_shift", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__cautious_shift","s":"ativo","d":"Cautious Shift","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__cautious_shift"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
