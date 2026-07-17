#!/usr/bin/env python3
"""Williams Syndrome"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/williams_syndrome", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_williams_syndrome","s":"ativo","d":"Williams Syndrome","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_williams_syndrome"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
