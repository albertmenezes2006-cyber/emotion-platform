#!/usr/bin/env python3
"""Unity Cialdini"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/unity_cialdini", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__unity_cialdini","s":"ativo","d":"Unity Cialdini","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__unity_cialdini"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
