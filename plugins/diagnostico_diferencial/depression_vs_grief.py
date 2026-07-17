#!/usr/bin/env python3
"""Depression Vs Grief"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/depression_vs_grief", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_depression_vs_grief","s":"ativo","d":"Depression Vs Grief","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_depression_vs_grief"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
