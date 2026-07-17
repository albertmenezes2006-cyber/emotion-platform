#!/usr/bin/env python3
"""Coercive Control Court"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/coercive_control_court", tags=["saude_mental_juridico_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_jurid_coercive_control_court","s":"ativo","d":"Coercive Control Court","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_jurid_coercive_control_court"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
