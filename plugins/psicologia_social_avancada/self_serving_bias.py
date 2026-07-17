#!/usr/bin/env python3
"""Self Serving Bias"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/self_serving_bias", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__self_serving_bias","s":"ativo","d":"Self Serving Bias","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__self_serving_bias"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
