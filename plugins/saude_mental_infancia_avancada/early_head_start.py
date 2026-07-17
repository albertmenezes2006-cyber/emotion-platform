#!/usr/bin/env python3
"""Early Head Start"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/early_head_start", tags=["saude_mental_infancia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_infan_early_head_start","s":"ativo","d":"Early Head Start","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_infan_early_head_start"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
