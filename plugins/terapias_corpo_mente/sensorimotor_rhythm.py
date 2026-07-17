#!/usr/bin/env python3
"""Sensorimotor Rhythm"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapias_cor/sensorimotor_rhythm", tags=["terapias_corpo_mente"])
@router.get("")
async def info():
    return JSONResponse({"p":"terapias_corpo_men_sensorimotor_rhythm","s":"ativo","d":"Sensorimotor Rhythm","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapias_corpo_men_sensorimotor_rhythm"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
