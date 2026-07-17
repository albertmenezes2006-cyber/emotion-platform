#!/usr/bin/env python3
"""Onboarding Psychology"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/onboarding_psychology", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_onboarding_psychology","s":"ativo","d":"Onboarding Psychology","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_onboarding_psychology"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
