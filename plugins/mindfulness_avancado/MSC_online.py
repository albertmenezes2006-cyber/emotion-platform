#!/usr/bin/env python3
"""Msc Online"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/MSC_online", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_MSC_online","s":"ativo","d":"Msc Online","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_MSC_online"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
