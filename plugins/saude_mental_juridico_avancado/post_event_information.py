#!/usr/bin/env python3
"""Post Event Information"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/post_event_information", tags=["saude_mental_juridico_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_jurid_post_event_information","s":"ativo","d":"Post Event Information","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_jurid_post_event_information"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
