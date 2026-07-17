#!/usr/bin/env python3
"""Saude Mental Singapura em saude mental internacional"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental_in/saude_mental_singapura", tags=["saude_mental_internacional"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"saude_mental_interna_saude_mental_singapura","status":"ativo","desc":"Saude Mental Singapura em saude mental internacional","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_interna_saude_mental_singapura"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
