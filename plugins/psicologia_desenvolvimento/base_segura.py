#!/usr/bin/env python3
"""Base Segura"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/base_segura", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_base_segura","s":"ativo","d":"Base Segura","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_base_segura"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
