#!/usr/bin/env python3
"""Warfarin Genetics"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/warfarin_genetics", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_warfarin_genetics","s":"ativo","d":"Warfarin Genetics","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_warfarin_genetics"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
