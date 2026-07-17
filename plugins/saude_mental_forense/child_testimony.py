#!/usr/bin/env python3
"""Child Testimony"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/child_testimony", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_child_testimony","s":"ativo","d":"Child Testimony","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_child_testimony"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
