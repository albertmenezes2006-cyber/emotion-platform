#!/usr/bin/env python3
"""Liking Principle2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/liking_principle2", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__liking_principle2","s":"ativo","d":"Liking Principle2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__liking_principle2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
