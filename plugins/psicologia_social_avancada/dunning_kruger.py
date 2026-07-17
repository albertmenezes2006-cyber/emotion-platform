#!/usr/bin/env python3
"""Dunning Kruger"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/dunning_kruger", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__dunning_kruger","s":"ativo","d":"Dunning Kruger","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__dunning_kruger"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
