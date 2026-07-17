#!/usr/bin/env python3
"""Sports Development"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/sports_development", tags=["saude_mental_infancia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_infan_sports_development","s":"ativo","d":"Sports Development","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_infan_sports_development"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
