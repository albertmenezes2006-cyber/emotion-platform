#!/usr/bin/env python3
"""Guilty Mind"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/guilty_mind", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_guilty_mind","s":"ativo","d":"Guilty Mind","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_guilty_mind"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
