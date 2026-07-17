#!/usr/bin/env python3
"""Falsa Crenca"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/falsa_crenca", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_falsa_crenca","s":"ativo","d":"Falsa Crenca","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_falsa_crenca"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
