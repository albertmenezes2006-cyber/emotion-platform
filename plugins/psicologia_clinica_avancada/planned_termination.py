#!/usr/bin/env python3
"""Planned Termination"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/planned_termination", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_planned_termination","s":"ativo","d":"Planned Termination","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_planned_termination"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
