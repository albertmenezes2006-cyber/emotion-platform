#!/usr/bin/env python3
"""Spiritual Care Elder"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/spiritual_care_elder", tags=["saude_mental_idoso_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_idoso_spiritual_care_elder","s":"ativo","d":"Spiritual Care Elder","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_idoso_spiritual_care_elder"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
