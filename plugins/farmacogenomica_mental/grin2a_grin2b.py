#!/usr/bin/env python3
"""Grin2A Grin2B"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/grin2a_grin2b", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_grin2a_grin2b","s":"ativo","d":"Grin2A Grin2B","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_grin2a_grin2b"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
