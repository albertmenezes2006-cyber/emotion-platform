#!/usr/bin/env python3
"""Nonviolent Communication2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/nonviolent_communication2", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_nonviolent_communication2","s":"ativo","d":"Nonviolent Communication2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_nonviolent_communication2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
