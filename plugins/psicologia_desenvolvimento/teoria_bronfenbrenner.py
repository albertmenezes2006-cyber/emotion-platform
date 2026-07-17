#!/usr/bin/env python3
"""Teoria Bronfenbrenner"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/teoria_bronfenbrenner", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_teoria_bronfenbrenner","s":"ativo","d":"Teoria Bronfenbrenner","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_teoria_bronfenbrenner"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
