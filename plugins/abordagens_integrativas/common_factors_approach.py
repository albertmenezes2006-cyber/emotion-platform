#!/usr/bin/env python3
"""Common Factors Approach"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/common_factors_approach", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_common_factors_approach","s":"ativo","d":"Common Factors Approach","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_common_factors_approach"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
