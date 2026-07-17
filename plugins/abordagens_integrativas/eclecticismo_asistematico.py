#!/usr/bin/env python3
"""Eclecticismo Asistematico"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/eclecticismo_asistematico", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_eclecticismo_asistematico","s":"ativo","d":"Eclecticismo Asistematico","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_eclecticismo_asistematico"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
