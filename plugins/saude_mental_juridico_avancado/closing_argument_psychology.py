#!/usr/bin/env python3
"""Closing Argument Psychology"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/closing_argument_psychology", tags=["saude_mental_juridico_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_jurid_closing_argument_psycholo","s":"ativo","d":"Closing Argument Psychology","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_jurid_closing_argument_psycholo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
