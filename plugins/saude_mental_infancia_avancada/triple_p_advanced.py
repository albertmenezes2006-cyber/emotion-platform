#!/usr/bin/env python3
"""Triple P Advanced"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/triple_p_advanced", tags=["saude_mental_infancia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_infan_triple_p_advanced","s":"ativo","d":"Triple P Advanced","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_infan_triple_p_advanced"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
