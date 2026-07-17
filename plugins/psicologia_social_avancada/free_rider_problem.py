#!/usr/bin/env python3
"""Free Rider Problem"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/free_rider_problem", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__free_rider_problem","s":"ativo","d":"Free Rider Problem","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__free_rider_problem"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
