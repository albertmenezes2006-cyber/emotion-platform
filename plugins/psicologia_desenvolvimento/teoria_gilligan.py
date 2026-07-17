#!/usr/bin/env python3
"""Teoria Gilligan"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/teoria_gilligan", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_teoria_gilligan","s":"ativo","d":"Teoria Gilligan","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_teoria_gilligan"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
