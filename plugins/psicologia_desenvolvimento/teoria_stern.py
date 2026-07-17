#!/usr/bin/env python3
"""Teoria Stern"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/teoria_stern", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_teoria_stern","s":"ativo","d":"Teoria Stern","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_teoria_stern"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
