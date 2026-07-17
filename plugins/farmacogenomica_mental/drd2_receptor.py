#!/usr/bin/env python3
"""Drd2 Receptor"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/drd2_receptor", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_drd2_receptor","s":"ativo","d":"Drd2 Receptor","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_drd2_receptor"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
