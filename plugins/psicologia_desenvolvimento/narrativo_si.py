#!/usr/bin/env python3
"""Narrativo Si"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/narrativo_si", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_narrativo_si","s":"ativo","d":"Narrativo Si","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_narrativo_si"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
