#!/usr/bin/env python3
"""Attachment Informed"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/attachment_informed", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_attachment_informed","s":"ativo","d":"Attachment Informed","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_attachment_informed"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
