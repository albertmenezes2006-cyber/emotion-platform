#!/usr/bin/env python3
"""Person Job Fit"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/person_job_fit", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_person_job_fit","s":"ativo","d":"Person Job Fit","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_person_job_fit"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
