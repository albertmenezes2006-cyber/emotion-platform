#!/usr/bin/env python3
"""Structural Family2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/structural_family2", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_structural_family2","s":"ativo","d":"Structural Family2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_structural_family2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
