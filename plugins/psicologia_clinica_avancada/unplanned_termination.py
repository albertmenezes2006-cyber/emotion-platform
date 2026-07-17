#!/usr/bin/env python3
"""Unplanned Termination"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/unplanned_termination", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_unplanned_termination","s":"ativo","d":"Unplanned Termination","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_unplanned_termination"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
