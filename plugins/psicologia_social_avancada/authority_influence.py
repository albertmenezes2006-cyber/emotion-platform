#!/usr/bin/env python3
"""Authority Influence"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/authority_influence", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__authority_influence","s":"ativo","d":"Authority Influence","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__authority_influence"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
