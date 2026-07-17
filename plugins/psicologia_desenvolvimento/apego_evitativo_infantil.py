#!/usr/bin/env python3
"""Apego Evitativo Infantil"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/apego_evitativo_infantil", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_apego_evitativo_infantil","s":"ativo","d":"Apego Evitativo Infantil","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_apego_evitativo_infantil"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
