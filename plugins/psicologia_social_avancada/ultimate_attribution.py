#!/usr/bin/env python3
"""Ultimate Attribution"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/ultimate_attribution", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__ultimate_attribution","s":"ativo","d":"Ultimate Attribution","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__ultimate_attribution"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
