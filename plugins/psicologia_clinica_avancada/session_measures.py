#!/usr/bin/env python3
"""Session Measures"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/session_measures", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_session_measures","s":"ativo","d":"Session Measures","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_session_measures"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
