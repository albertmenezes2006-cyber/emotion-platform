#!/usr/bin/env python3
"""Positive Self Talk"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/positive_self_talk", tags=["saude_mental_esporte"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_espor_positive_self_talk","s":"ativo","d":"Positive Self Talk","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_espor_positive_self_talk"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
