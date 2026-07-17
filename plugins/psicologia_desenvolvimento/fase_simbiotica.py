#!/usr/bin/env python3
"""Fase Simbiotica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/fase_simbiotica", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_fase_simbiotica","s":"ativo","d":"Fase Simbiotica","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_fase_simbiotica"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
