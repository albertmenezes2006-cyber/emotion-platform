#!/usr/bin/env python3
"""5P Formulation"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/5p_formulation", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_5p_formulation","s":"ativo","d":"5P Formulation","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_5p_formulation"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
