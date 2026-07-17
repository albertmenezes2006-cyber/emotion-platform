#!/usr/bin/env python3
"""Cognitive Ability Test"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/cognitive_ability_test", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_cognitive_ability_test","s":"ativo","d":"Cognitive Ability Test","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_cognitive_ability_test"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
