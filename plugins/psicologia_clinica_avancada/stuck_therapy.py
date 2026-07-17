#!/usr/bin/env python3
"""Stuck Therapy"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/stuck_therapy", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_stuck_therapy","s":"ativo","d":"Stuck Therapy","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_stuck_therapy"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
