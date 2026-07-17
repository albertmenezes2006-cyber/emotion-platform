#!/usr/bin/env python3
"""Teoria Vygotsky"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/teoria_vygotsky", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_teoria_vygotsky","s":"ativo","d":"Teoria Vygotsky","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_teoria_vygotsky"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
