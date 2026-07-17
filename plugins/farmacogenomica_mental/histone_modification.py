#!/usr/bin/env python3
"""Histone Modification"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/histone_modification", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_histone_modification","s":"ativo","d":"Histone Modification","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_histone_modification"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
