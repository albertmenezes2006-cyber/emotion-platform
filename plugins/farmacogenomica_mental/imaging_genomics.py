#!/usr/bin/env python3
"""Imaging Genomics"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/imaging_genomics", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_imaging_genomics","s":"ativo","d":"Imaging Genomics","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_imaging_genomics"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
