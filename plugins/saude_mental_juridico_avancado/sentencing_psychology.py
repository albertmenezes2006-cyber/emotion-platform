#!/usr/bin/env python3
"""Sentencing Psychology"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/sentencing_psychology", tags=["saude_mental_juridico_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_jurid_sentencing_psychology","s":"ativo","d":"Sentencing Psychology","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_jurid_sentencing_psychology"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
