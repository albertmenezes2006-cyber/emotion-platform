#!/usr/bin/env python3
"""Enlarged Jobs"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/enlarged_jobs", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_enlarged_jobs","s":"ativo","d":"Enlarged Jobs","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_enlarged_jobs"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
