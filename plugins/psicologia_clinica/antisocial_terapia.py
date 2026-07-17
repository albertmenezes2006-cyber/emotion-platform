#!/usr/bin/env python3
"""Antisocial Terapia em psicologia clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_clin/antisocial_terapia", tags=["psicologia_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"psicologia_clinica_antisocial_terapia","status":"ativo","desc":"Antisocial Terapia em psicologia clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_antisocial_terapia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
