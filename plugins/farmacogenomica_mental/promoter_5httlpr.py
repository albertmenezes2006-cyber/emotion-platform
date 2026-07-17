#!/usr/bin/env python3
"""Promoter 5Httlpr"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/promoter_5httlpr", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_promoter_5httlpr","s":"ativo","d":"Promoter 5Httlpr","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_promoter_5httlpr"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
