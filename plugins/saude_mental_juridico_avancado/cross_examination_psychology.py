#!/usr/bin/env python3
"""Cross Examination Psychology"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/cross_examination_psychology", tags=["saude_mental_juridico_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_jurid_cross_examination_psychol","s":"ativo","d":"Cross Examination Psychology","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_jurid_cross_examination_psychol"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
