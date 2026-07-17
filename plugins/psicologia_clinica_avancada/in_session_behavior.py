#!/usr/bin/env python3
"""In Session Behavior"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/in_session_behavior", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_in_session_behavior","s":"ativo","d":"In Session Behavior","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_in_session_behavior"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
