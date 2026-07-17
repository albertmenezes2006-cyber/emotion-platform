#!/usr/bin/env python3
"""Stimulant Genetics"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/stimulant_genetics", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_stimulant_genetics","s":"ativo","d":"Stimulant Genetics","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_stimulant_genetics"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
