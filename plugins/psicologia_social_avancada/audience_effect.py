#!/usr/bin/env python3
"""Audience Effect"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/audience_effect", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__audience_effect","s":"ativo","d":"Audience Effect","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__audience_effect"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
