#!/usr/bin/env python3
"""Non Judgmental Mind"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/non_judgmental_mind", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_non_judgmental_mind","s":"ativo","d":"Non Judgmental Mind","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_non_judgmental_mind"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
