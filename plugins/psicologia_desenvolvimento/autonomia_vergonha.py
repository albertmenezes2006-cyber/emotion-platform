#!/usr/bin/env python3
"""Autonomia Vergonha"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/autonomia_vergonha", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_autonomia_vergonha","s":"ativo","d":"Autonomia Vergonha","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_autonomia_vergonha"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
