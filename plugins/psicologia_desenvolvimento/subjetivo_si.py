#!/usr/bin/env python3
"""Subjetivo Si"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/subjetivo_si", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_subjetivo_si","s":"ativo","d":"Subjetivo Si","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_subjetivo_si"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
