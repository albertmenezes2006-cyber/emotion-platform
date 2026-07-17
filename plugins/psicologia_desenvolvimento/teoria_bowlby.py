#!/usr/bin/env python3
"""Teoria Bowlby"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/teoria_bowlby", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_teoria_bowlby","s":"ativo","d":"Teoria Bowlby","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_teoria_bowlby"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
