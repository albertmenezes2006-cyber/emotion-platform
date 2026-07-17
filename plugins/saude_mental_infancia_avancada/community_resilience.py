#!/usr/bin/env python3
"""Community Resilience"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/community_resilience", tags=["saude_mental_infancia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_infan_community_resilience","s":"ativo","d":"Community Resilience","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_infan_community_resilience"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
