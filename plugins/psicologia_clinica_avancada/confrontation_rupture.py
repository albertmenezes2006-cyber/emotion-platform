#!/usr/bin/env python3
"""Confrontation Rupture"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/confrontation_rupture", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_confrontation_rupture","s":"ativo","d":"Confrontation Rupture","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_confrontation_rupture"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
