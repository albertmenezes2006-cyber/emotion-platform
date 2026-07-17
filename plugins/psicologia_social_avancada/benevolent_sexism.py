#!/usr/bin/env python3
"""Benevolent Sexism"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/benevolent_sexism", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__benevolent_sexism","s":"ativo","d":"Benevolent Sexism","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__benevolent_sexism"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
