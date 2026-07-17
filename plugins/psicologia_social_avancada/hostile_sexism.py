#!/usr/bin/env python3
"""Hostile Sexism"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/hostile_sexism", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__hostile_sexism","s":"ativo","d":"Hostile Sexism","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__hostile_sexism"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
