#!/usr/bin/env python3
"""Serum Levels"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/serum_levels", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_serum_levels","s":"ativo","d":"Serum Levels","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_serum_levels"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
