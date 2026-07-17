#!/usr/bin/env python3
"""Glass Ceiling2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/glass_ceiling2", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__glass_ceiling2","s":"ativo","d":"Glass Ceiling2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__glass_ceiling2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
