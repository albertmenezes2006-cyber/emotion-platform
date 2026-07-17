#!/usr/bin/env python3
"""Efficacy Research"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/efficacy_research", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_efficacy_research","s":"ativo","d":"Efficacy Research","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_efficacy_research"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
