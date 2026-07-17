#!/usr/bin/env python3
"""Feigning Ptsd"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/feigning_ptsd", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_feigning_ptsd","s":"ativo","d":"Feigning Ptsd","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_feigning_ptsd"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
