#!/usr/bin/env python3
"""Common Humanity Practice"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/common_humanity_practice", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_common_humanity_practice","s":"ativo","d":"Common Humanity Practice","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_common_humanity_practice"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
