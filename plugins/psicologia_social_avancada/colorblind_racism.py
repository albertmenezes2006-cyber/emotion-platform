#!/usr/bin/env python3
"""Colorblind Racism"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/colorblind_racism", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__colorblind_racism","s":"ativo","d":"Colorblind Racism","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__colorblind_racism"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
