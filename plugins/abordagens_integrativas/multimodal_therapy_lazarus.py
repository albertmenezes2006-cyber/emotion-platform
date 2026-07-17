#!/usr/bin/env python3
"""Multimodal Therapy Lazarus"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/multimodal_therapy_lazarus", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_multimodal_therapy_lazaru","s":"ativo","d":"Multimodal Therapy Lazarus","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_multimodal_therapy_lazaru"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
