#!/usr/bin/env python3
"""Job Analysis"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/job_analysis", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_job_analysis","s":"ativo","d":"Job Analysis","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_job_analysis"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
