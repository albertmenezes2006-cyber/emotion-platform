#!/usr/bin/env python3
"""Spj Approach"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/spj_approach", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_spj_approach","s":"ativo","d":"Spj Approach","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_spj_approach"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
