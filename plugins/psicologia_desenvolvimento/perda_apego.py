#!/usr/bin/env python3
"""Perda Apego"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/perda_apego", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_perda_apego","s":"ativo","d":"Perda Apego","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_perda_apego"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
