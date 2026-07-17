#!/usr/bin/env python3
"""Imago Therapy"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/imago_therapy", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_imago_therapy","s":"ativo","d":"Imago Therapy","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_imago_therapy"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
