#!/usr/bin/env python3
"""Cluster Suicide Media"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/cluster_suicide_media", tags=["saude_mental_midia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_midia_cluster_suicide_media","s":"ativo","d":"Cluster Suicide Media","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_midia_cluster_suicide_media"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
