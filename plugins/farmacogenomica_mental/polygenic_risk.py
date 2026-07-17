#!/usr/bin/env python3
"""Polygenic Risk"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/polygenic_risk", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_polygenic_risk","s":"ativo","d":"Polygenic Risk","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_polygenic_risk"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
