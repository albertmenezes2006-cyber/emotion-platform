#!/usr/bin/env python3
"""Randomized Controlled"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/randomized_controlled", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_randomized_controlled","s":"ativo","d":"Randomized Controlled","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_randomized_controlled"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
