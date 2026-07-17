#!/usr/bin/env python3
"""Grik1 Grik2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/grik1_grik2", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_grik1_grik2","s":"ativo","d":"Grik1 Grik2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_grik1_grik2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
