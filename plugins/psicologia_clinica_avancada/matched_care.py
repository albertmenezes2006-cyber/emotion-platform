#!/usr/bin/env python3
"""Matched Care"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/matched_care", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_matched_care","s":"ativo","d":"Matched Care","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_matched_care"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
