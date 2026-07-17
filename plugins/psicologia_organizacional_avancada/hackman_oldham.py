#!/usr/bin/env python3
"""Hackman Oldham"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/hackman_oldham", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_hackman_oldham","s":"ativo","d":"Hackman Oldham","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_hackman_oldham"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
