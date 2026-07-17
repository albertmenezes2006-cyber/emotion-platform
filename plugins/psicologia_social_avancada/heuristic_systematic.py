#!/usr/bin/env python3
"""Heuristic Systematic"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/heuristic_systematic", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__heuristic_systematic","s":"ativo","d":"Heuristic Systematic","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__heuristic_systematic"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
