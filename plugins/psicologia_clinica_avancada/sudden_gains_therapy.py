#!/usr/bin/env python3
"""Sudden Gains Therapy"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/sudden_gains_therapy", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_sudden_gains_therapy","s":"ativo","d":"Sudden Gains Therapy","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_sudden_gains_therapy"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
