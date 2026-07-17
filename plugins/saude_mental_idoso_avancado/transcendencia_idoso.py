#!/usr/bin/env python3
"""Transcendencia Idoso"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/transcendencia_idoso", tags=["saude_mental_idoso_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_idoso_transcendencia_idoso","s":"ativo","d":"Transcendencia Idoso","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_idoso_transcendencia_idoso"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
