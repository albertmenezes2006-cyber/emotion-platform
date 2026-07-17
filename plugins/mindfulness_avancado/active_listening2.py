#!/usr/bin/env python3
"""Active Listening2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/active_listening2", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_active_listening2","s":"ativo","d":"Active Listening2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_active_listening2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
