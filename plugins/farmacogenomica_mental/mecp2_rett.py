#!/usr/bin/env python3
"""Mecp2 Rett"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/mecp2_rett", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_mecp2_rett","s":"ativo","d":"Mecp2 Rett","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_mecp2_rett"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
