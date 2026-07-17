#!/usr/bin/env python3
"""Transportation Theory"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/transportation_theory", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__transportation_theory","s":"ativo","d":"Transportation Theory","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__transportation_theory"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
