#!/usr/bin/env python3
"""Number Needed Treat"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/number_needed_treat", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_number_needed_treat","s":"ativo","d":"Number Needed Treat","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_number_needed_treat"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
