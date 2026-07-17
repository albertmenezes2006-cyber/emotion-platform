#!/usr/bin/env python3
"""Eye Tracking Mental em saude mental digital avancado"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental_di/eye_tracking_mental", tags=["saude_mental_digital_avancado"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"saude_mental_digital_eye_tracking_mental","status":"ativo","desc":"Eye Tracking Mental em saude mental digital avancado","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_digital_eye_tracking_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
