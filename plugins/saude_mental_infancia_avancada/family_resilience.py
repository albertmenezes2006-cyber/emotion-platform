#!/usr/bin/env python3
"""Family Resilience"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/family_resilience", tags=["saude_mental_infancia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_infan_family_resilience","s":"ativo","d":"Family Resilience","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_infan_family_resilience"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
