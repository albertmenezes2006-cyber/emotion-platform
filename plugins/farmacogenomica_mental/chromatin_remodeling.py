#!/usr/bin/env python3
"""Chromatin Remodeling"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/chromatin_remodeling", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_chromatin_remodeling","s":"ativo","d":"Chromatin Remodeling","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_chromatin_remodeling"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
