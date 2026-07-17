#!/usr/bin/env python3
"""Genovese Syndrome"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/genovese_syndrome", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__genovese_syndrome","s":"ativo","d":"Genovese Syndrome","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__genovese_syndrome"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
