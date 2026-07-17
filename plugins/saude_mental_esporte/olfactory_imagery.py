#!/usr/bin/env python3
"""Olfactory Imagery"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/olfactory_imagery", tags=["saude_mental_esporte"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_espor_olfactory_imagery","s":"ativo","d":"Olfactory Imagery","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_espor_olfactory_imagery"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
