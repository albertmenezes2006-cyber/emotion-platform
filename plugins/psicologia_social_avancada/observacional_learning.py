#!/usr/bin/env python3
"""Observacional Learning"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/observacional_learning", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__observacional_learning","s":"ativo","d":"Observacional Learning","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__observacional_learning"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
