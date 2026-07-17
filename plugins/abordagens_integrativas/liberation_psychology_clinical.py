#!/usr/bin/env python3
"""Liberation Psychology Clinical"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/liberation_psychology_clinic", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_liberation_psychology_cli","s":"ativo","d":"Liberation Psychology Clinical","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_liberation_psychology_cli"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
