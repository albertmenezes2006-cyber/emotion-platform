#!/usr/bin/env python3
"""Mindfulness Based Relapse"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/mindfulness_based_relapse", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_mindfulness_based_relapse","s":"ativo","d":"Mindfulness Based Relapse","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_mindfulness_based_relapse"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
