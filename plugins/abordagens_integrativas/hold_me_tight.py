#!/usr/bin/env python3
"""Hold Me Tight"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/hold_me_tight", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_hold_me_tight","s":"ativo","d":"Hold Me Tight","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_hold_me_tight"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
