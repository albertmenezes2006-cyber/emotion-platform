#!/usr/bin/env python3
"""False Confession"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/false_confession", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_false_confession","s":"ativo","d":"False Confession","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_false_confession"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
