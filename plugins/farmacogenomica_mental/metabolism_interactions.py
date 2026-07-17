#!/usr/bin/env python3
"""Metabolism Interactions"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/metabolism_interactions", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_metabolism_interactions","s":"ativo","d":"Metabolism Interactions","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_metabolism_interactions"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
