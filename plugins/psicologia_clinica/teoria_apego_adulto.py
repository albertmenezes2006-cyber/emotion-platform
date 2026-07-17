#!/usr/bin/env python3
"""Teoria Apego Adulto em psicologia clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_clin/teoria_apego_adulto", tags=["psicologia_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"psicologia_clinica_teoria_apego_adulto","status":"ativo","desc":"Teoria Apego Adulto em psicologia clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_teoria_apego_adulto"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
