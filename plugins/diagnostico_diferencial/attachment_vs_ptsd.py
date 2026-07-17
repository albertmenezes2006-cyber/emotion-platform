#!/usr/bin/env python3
"""Attachment Vs Ptsd"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/attachment_vs_ptsd", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_attachment_vs_ptsd","s":"ativo","d":"Attachment Vs Ptsd","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_attachment_vs_ptsd"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
