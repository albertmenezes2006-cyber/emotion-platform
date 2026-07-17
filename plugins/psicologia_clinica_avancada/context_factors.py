#!/usr/bin/env python3
"""Context Factors"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/context_factors", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_context_factors","s":"ativo","d":"Context Factors","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_context_factors"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
