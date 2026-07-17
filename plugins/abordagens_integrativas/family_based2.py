#!/usr/bin/env python3
"""Family Based2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/family_based2", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_family_based2","s":"ativo","d":"Family Based2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_family_based2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
