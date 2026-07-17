#!/usr/bin/env python3
"""Luto Apego"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/luto_apego", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_luto_apego","s":"ativo","d":"Luto Apego","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_luto_apego"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
