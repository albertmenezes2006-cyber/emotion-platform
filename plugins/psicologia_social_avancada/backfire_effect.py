#!/usr/bin/env python3
"""Backfire Effect"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/backfire_effect", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__backfire_effect","s":"ativo","d":"Backfire Effect","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__backfire_effect"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
