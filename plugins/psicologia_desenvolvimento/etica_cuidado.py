#!/usr/bin/env python3
"""Etica Cuidado"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/etica_cuidado", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_etica_cuidado","s":"ativo","d":"Etica Cuidado","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_etica_cuidado"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
