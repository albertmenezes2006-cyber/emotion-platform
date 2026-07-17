#!/usr/bin/env python3
"""Minimal Group"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/minimal_group", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__minimal_group","s":"ativo","d":"Minimal Group","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__minimal_group"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
