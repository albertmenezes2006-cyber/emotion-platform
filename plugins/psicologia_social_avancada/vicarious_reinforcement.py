#!/usr/bin/env python3
"""Vicarious Reinforcement"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/vicarious_reinforcement", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__vicarious_reinforcement","s":"ativo","d":"Vicarious Reinforcement","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__vicarious_reinforcement"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
