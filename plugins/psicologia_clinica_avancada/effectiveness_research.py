#!/usr/bin/env python3
"""Effectiveness Research"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/effectiveness_research", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_effectiveness_research","s":"ativo","d":"Effectiveness Research","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_effectiveness_research"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
