#!/usr/bin/env python3
"""Capacidade Civil2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/capacidade_civil2", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_capacidade_civil2","s":"ativo","d":"Capacidade Civil2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_capacidade_civil2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
