#!/usr/bin/env python3
"""Interview Validity"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/interview_validity", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_interview_validity","s":"ativo","d":"Interview Validity","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_interview_validity"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
