#!/usr/bin/env python3
"""Practitioner Researcher"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/practitioner_researcher", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_practitioner_researcher","s":"ativo","d":"Practitioner Researcher","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_practitioner_researcher"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
