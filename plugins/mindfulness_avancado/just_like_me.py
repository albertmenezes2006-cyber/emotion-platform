#!/usr/bin/env python3
"""Just Like Me"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/just_like_me", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_just_like_me","s":"ativo","d":"Just Like Me","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_just_like_me"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
