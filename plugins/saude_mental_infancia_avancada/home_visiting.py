#!/usr/bin/env python3
"""Home Visiting"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/home_visiting", tags=["saude_mental_infancia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_infan_home_visiting","s":"ativo","d":"Home Visiting","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_infan_home_visiting"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
