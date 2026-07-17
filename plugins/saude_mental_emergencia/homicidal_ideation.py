#!/usr/bin/env python3
"""Homicidal Ideation"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/homicidal_ideation", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_homicidal_ideation","s":"ativo","d":"Homicidal Ideation","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_homicidal_ideation"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
