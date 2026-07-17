#!/usr/bin/env python3
"""Bdnf Val66Met"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/bdnf_val66met", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_bdnf_val66met","s":"ativo","d":"Bdnf Val66Met","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_bdnf_val66met"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
