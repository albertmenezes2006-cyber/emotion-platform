#!/usr/bin/env python3
"""Emdr Somatic"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/EMDR_somatic", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_EMDR_somatic","s":"ativo","d":"Emdr Somatic","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_EMDR_somatic"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
