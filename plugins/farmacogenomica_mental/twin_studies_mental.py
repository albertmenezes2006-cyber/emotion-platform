#!/usr/bin/env python3
"""Twin Studies Mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/twin_studies_mental", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_twin_studies_mental","s":"ativo","d":"Twin Studies Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_twin_studies_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
