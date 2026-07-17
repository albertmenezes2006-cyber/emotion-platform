#!/usr/bin/env python3
"""Endophenotype"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/endophenotype", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_endophenotype","s":"ativo","d":"Endophenotype","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_endophenotype"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
