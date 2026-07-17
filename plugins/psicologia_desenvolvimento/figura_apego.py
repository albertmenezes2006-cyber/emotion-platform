#!/usr/bin/env python3
"""Figura Apego"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/figura_apego", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_figura_apego","s":"ativo","d":"Figura Apego","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_figura_apego"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
