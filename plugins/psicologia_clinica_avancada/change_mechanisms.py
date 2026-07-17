#!/usr/bin/env python3
"""Change Mechanisms"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/change_mechanisms", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_change_mechanisms","s":"ativo","d":"Change Mechanisms","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_change_mechanisms"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
