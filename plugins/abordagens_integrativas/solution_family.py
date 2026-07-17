#!/usr/bin/env python3
"""Solution Family"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/solution_family", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_solution_family","s":"ativo","d":"Solution Family","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_solution_family"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
