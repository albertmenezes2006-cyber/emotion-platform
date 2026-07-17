#!/usr/bin/env python3
"""Reliable Change Index"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/reliable_change_index", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_reliable_change_index","s":"ativo","d":"Reliable Change Index","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_reliable_change_index"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
