#!/usr/bin/env python3
"""Terapia Baseada Apego em psicologia clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_clin/terapia_baseada_apego", tags=["psicologia_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"psicologia_clinica_terapia_baseada_apego","status":"ativo","desc":"Terapia Baseada Apego em psicologia clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_terapia_baseada_apego"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
