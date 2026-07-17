#!/usr/bin/env python3
"""Functional Family"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/functional_family", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_functional_family","s":"ativo","d":"Functional Family","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_functional_family"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
