#!/usr/bin/env python3
"""Surf Urge"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/surf_urge", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_surf_urge","s":"ativo","d":"Surf Urge","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_surf_urge"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
