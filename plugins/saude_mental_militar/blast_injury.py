#!/usr/bin/env python3
"""Blast Injury"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/blast_injury", tags=["saude_mental_militar"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_milit_blast_injury","s":"ativo","d":"Blast Injury","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_milit_blast_injury"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
