#!/usr/bin/env python3
"""Interdição Legal"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/interdição_legal", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_interdição_legal","s":"ativo","d":"Interdição Legal","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_interdição_legal"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
