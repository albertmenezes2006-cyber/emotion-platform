#!/usr/bin/env python3
"""Apego Fearful Avoidant em psicologia clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_clin/apego_fearful_avoidant", tags=["psicologia_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"psicologia_clinica_apego_fearful_avoidant","status":"ativo","desc":"Apego Fearful Avoidant em psicologia clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_apego_fearful_avoidant"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
