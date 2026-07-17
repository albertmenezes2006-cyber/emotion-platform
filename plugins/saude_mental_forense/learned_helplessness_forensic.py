#!/usr/bin/env python3
"""Learned Helplessness Forensic"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/learned_helplessness_forensi", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_learned_helplessness_fore","s":"ativo","d":"Learned Helplessness Forensic","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_learned_helplessness_fore"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
