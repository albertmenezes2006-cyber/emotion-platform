#!/usr/bin/env python3
"""Dispositional Attribution"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/dispositional_attribution", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__dispositional_attribution","s":"ativo","d":"Dispositional Attribution","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__dispositional_attribution"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
