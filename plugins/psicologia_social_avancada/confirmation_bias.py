#!/usr/bin/env python3
"""Confirmation Bias"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/confirmation_bias", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__confirmation_bias","s":"ativo","d":"Confirmation Bias","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__confirmation_bias"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
