#!/usr/bin/env python3
"""Job Crafting2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/job_crafting2", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_job_crafting2","s":"ativo","d":"Job Crafting2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_job_crafting2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
