#!/usr/bin/env python3
"""Treatment Resistant"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/treatment_resistant", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_treatment_resistant","s":"ativo","d":"Treatment Resistant","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_treatment_resistant"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
