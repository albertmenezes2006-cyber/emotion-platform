#!/usr/bin/env python3
"""Diminished Responsibility"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/diminished_responsibility", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_diminished_responsibility","s":"ativo","d":"Diminished Responsibility","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_diminished_responsibility"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
