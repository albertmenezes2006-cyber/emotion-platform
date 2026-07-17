#!/usr/bin/env python3
"""Internal Validity"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/internal_validity", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_internal_validity","s":"ativo","d":"Internal Validity","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_internal_validity"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
