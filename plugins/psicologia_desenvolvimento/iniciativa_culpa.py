#!/usr/bin/env python3
"""Iniciativa Culpa"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/iniciativa_culpa", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_iniciativa_culpa","s":"ativo","d":"Iniciativa Culpa","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_iniciativa_culpa"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
