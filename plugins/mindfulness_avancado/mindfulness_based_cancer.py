#!/usr/bin/env python3
"""Mindfulness Based Cancer"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/mindfulness_based_cancer", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_mindfulness_based_cancer","s":"ativo","d":"Mindfulness Based Cancer","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_mindfulness_based_cancer"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
