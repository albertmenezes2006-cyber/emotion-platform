#!/usr/bin/env python3
"""Store And Forward em saude mental digital avancado"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental_di/store_and_forward", tags=["saude_mental_digital_avancado"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"saude_mental_digital_store_and_forward","status":"ativo","desc":"Store And Forward em saude mental digital avancado","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_digital_store_and_forward"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
