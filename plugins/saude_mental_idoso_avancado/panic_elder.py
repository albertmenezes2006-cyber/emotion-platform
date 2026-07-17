#!/usr/bin/env python3
"""Panic Elder"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/panic_elder", tags=["saude_mental_idoso_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_idoso_panic_elder","s":"ativo","d":"Panic Elder","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_idoso_panic_elder"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
