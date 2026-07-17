#!/usr/bin/env python3
"""Anchoring Bias"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/anchoring_bias", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__anchoring_bias","s":"ativo","d":"Anchoring Bias","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__anchoring_bias"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
