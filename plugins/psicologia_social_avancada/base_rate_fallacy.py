#!/usr/bin/env python3
"""Base Rate Fallacy"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/base_rate_fallacy", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__base_rate_fallacy","s":"ativo","d":"Base Rate Fallacy","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__base_rate_fallacy"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
