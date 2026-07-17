#!/usr/bin/env python3
"""Prejudice Reduction"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/prejudice_reduction", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__prejudice_reduction","s":"ativo","d":"Prejudice Reduction","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__prejudice_reduction"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
