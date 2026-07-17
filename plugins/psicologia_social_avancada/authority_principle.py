#!/usr/bin/env python3
"""Authority Principle"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/authority_principle", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__authority_principle","s":"ativo","d":"Authority Principle","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__authority_principle"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
