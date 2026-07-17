#!/usr/bin/env python3
"""Avoidance Goals"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/avoidance_goals", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_avoidance_goals","s":"ativo","d":"Avoidance Goals","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_avoidance_goals"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
