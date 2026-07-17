#!/usr/bin/env python3
"""Research Practitioner"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/research_practitioner", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_research_practitioner","s":"ativo","d":"Research Practitioner","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_research_practitioner"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
