#!/usr/bin/env python3
"""Gottman Method"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/gottman_method", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_gottman_method","s":"ativo","d":"Gottman Method","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_gottman_method"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
