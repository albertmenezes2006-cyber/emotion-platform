#!/usr/bin/env python3
"""Preference Organization"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/preference_organization", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_preference_organization","s":"ativo","d":"Preference Organization","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_preference_organization"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
