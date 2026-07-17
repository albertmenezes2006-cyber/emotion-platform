#!/usr/bin/env python3
"""Mente Reflexiva"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/mente_reflexiva", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_mente_reflexiva","s":"ativo","d":"Mente Reflexiva","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_mente_reflexiva"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
