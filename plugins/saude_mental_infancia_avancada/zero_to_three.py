#!/usr/bin/env python3
"""Zero To Three"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/zero_to_three", tags=["saude_mental_infancia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_infan_zero_to_three","s":"ativo","d":"Zero To Three","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_infan_zero_to_three"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
