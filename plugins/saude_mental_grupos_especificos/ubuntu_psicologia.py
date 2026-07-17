#!/usr/bin/env python3
"""Ubuntu Psicologia em saude mental grupos especificos"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental_gr/ubuntu_psicologia", tags=["saude_mental_grupos_especificos"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"saude_mental_grupos__ubuntu_psicologia","status":"ativo","desc":"Ubuntu Psicologia em saude mental grupos especificos","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_grupos__ubuntu_psicologia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
