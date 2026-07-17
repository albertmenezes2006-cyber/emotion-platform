#!/usr/bin/env python3
"""Conscientiousness"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/conscientiousness", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_conscientiousness","s":"ativo","d":"Conscientiousness","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_conscientiousness"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
