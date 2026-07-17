#!/usr/bin/env python3
"""Esprit De Corps"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/esprit_de_corps", tags=["saude_mental_militar"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_milit_esprit_de_corps","s":"ativo","d":"Esprit De Corps","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_milit_esprit_de_corps"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
