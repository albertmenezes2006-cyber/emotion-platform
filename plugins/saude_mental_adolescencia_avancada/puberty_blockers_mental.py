#!/usr/bin/env python3
"""Puberty Blockers Mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/puberty_blockers_mental", tags=["saude_mental_adolescencia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_adole_puberty_blockers_mental","s":"ativo","d":"Puberty Blockers Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_adole_puberty_blockers_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
