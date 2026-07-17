#!/usr/bin/env python3
"""Competence Work"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/competence_work", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_competence_work","s":"ativo","d":"Competence Work","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_competence_work"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
