#!/usr/bin/env python3
"""Productive Aging"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/productive_aging", tags=["saude_mental_idoso_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_idoso_productive_aging","s":"ativo","d":"Productive Aging","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_idoso_productive_aging"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
