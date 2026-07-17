#!/usr/bin/env python3
"""Bullying Desenvolvimento"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/bullying_desenvolvimento", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_bullying_desenvolvimento","s":"ativo","d":"Bullying Desenvolvimento","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_bullying_desenvolvimento"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
