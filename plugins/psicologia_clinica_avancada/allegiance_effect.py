#!/usr/bin/env python3
"""Allegiance Effect"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/allegiance_effect", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_allegiance_effect","s":"ativo","d":"Allegiance Effect","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_allegiance_effect"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
