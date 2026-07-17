#!/usr/bin/env python3
"""Early Childhood Mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/early_childhood_mental", tags=["saude_mental_infancia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_infan_early_childhood_mental","s":"ativo","d":"Early Childhood Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_infan_early_childhood_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
