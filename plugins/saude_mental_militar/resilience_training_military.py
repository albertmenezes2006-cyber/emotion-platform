#!/usr/bin/env python3
"""Resilience Training Military"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/resilience_training_military", tags=["saude_mental_militar"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_milit_resilience_training_milit","s":"ativo","d":"Resilience Training Military","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_milit_resilience_training_milit"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
