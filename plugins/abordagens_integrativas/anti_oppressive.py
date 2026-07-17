#!/usr/bin/env python3
"""Anti Oppressive"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/anti_oppressive", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_anti_oppressive","s":"ativo","d":"Anti Oppressive","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_anti_oppressive"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
