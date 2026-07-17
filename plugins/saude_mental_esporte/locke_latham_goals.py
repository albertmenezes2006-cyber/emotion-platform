#!/usr/bin/env python3
"""Locke Latham Goals"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/locke_latham_goals", tags=["saude_mental_esporte"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_espor_locke_latham_goals","s":"ativo","d":"Locke Latham Goals","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_espor_locke_latham_goals"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
