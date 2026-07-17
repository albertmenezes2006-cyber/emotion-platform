#!/usr/bin/env python3
"""Resilient Military Kid"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/resilient_military_kid", tags=["saude_mental_militar"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_milit_resilient_military_kid","s":"ativo","d":"Resilient Military Kid","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_milit_resilient_military_kid"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
