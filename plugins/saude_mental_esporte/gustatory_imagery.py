#!/usr/bin/env python3
"""Gustatory Imagery"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/gustatory_imagery", tags=["saude_mental_esporte"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_espor_gustatory_imagery","s":"ativo","d":"Gustatory Imagery","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_espor_gustatory_imagery"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
