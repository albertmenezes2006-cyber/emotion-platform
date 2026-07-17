#!/usr/bin/env python3
"""Desenvolvimento Sociocultural"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/desenvolvimento_sociocultura", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_desenvolvimento_sociocult","s":"ativo","d":"Desenvolvimento Sociocultural","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_desenvolvimento_sociocult"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
