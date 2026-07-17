#!/usr/bin/env python3
"""Temperamento Dif"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/temperamento_dif", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_temperamento_dif","s":"ativo","d":"Temperamento Dif","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_temperamento_dif"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
