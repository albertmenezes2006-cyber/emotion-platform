#!/usr/bin/env python3
"""Reasonable Mind2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/reasonable_mind2", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_reasonable_mind2","s":"ativo","d":"Reasonable Mind2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_reasonable_mind2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
