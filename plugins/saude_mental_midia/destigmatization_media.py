#!/usr/bin/env python3
"""Destigmatization Media"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/destigmatization_media", tags=["saude_mental_midia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_midia_destigmatization_media","s":"ativo","d":"Destigmatization Media","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_midia_destigmatization_media"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
