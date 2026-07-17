#!/usr/bin/env python3
"""Burnout Sport2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/burnout_sport2", tags=["saude_mental_esporte"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_espor_burnout_sport2","s":"ativo","d":"Burnout Sport2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_espor_burnout_sport2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
