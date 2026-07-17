#!/usr/bin/env python3
"""Newcomer Adjustment"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/newcomer_adjustment", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_newcomer_adjustment","s":"ativo","d":"Newcomer Adjustment","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_newcomer_adjustment"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
