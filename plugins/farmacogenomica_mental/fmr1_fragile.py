#!/usr/bin/env python3
"""Fmr1 Fragile"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/fmr1_fragile", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_fmr1_fragile","s":"ativo","d":"Fmr1 Fragile","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_fmr1_fragile"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
