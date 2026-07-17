#!/usr/bin/env python3
"""Conscious Communication"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/conscious_communication", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_conscious_communication","s":"ativo","d":"Conscious Communication","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_conscious_communication"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
