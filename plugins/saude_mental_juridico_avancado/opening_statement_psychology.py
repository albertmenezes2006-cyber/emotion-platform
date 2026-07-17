#!/usr/bin/env python3
"""Opening Statement Psychology"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/opening_statement_psychology", tags=["saude_mental_juridico_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_jurid_opening_statement_psychol","s":"ativo","d":"Opening Statement Psychology","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_jurid_opening_statement_psychol"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
