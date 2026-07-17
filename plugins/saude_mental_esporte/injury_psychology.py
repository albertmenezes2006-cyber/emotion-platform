#!/usr/bin/env python3
"""Injury Psychology"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/injury_psychology", tags=["saude_mental_esporte"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_espor_injury_psychology","s":"ativo","d":"Injury Psychology","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_espor_injury_psychology"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
