#!/usr/bin/env python3
"""Integracao Tecnica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/integracao_tecnica", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_integracao_tecnica","s":"ativo","d":"Integracao Tecnica","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_integracao_tecnica"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
