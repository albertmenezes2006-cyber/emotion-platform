#!/usr/bin/env python3
"""Istanbul Protocol"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/istanbul_protocol", tags=["saude_mental_juridico_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_jurid_istanbul_protocol","s":"ativo","d":"Istanbul Protocol","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_jurid_istanbul_protocol"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
