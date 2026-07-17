#!/usr/bin/env python3
"""Depression Vs Cyclothymia"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/depression_vs_cyclothymia", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_depression_vs_cyclothymia","s":"ativo","d":"Depression Vs Cyclothymia","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_depression_vs_cyclothymia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
