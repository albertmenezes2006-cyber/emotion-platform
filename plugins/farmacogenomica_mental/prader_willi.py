#!/usr/bin/env python3
"""Prader Willi"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/prader_willi", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_prader_willi","s":"ativo","d":"Prader Willi","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_prader_willi"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
