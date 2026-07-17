#!/usr/bin/env python3
"""Cross Sectional Formulation"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/cross_sectional_formulation", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_cross_sectional_formulati","s":"ativo","d":"Cross Sectional Formulation","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_cross_sectional_formulati"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
