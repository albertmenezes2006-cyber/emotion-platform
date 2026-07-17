#!/usr/bin/env python3
"""Client Factors"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/client_factors", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_client_factors","s":"ativo","d":"Client Factors","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_client_factors"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
