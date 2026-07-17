#!/usr/bin/env python3
"""Loading Dose"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/loading_dose", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_loading_dose","s":"ativo","d":"Loading Dose","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_loading_dose"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
