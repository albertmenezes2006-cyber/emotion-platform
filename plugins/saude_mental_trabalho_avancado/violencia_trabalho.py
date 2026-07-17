#!/usr/bin/env python3
"""Violencia Trabalho em saude mental trabalho avancado"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental_tr/violencia_trabalho", tags=["saude_mental_trabalho_avancado"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"saude_mental_trabalh_violencia_trabalho","status":"ativo","desc":"Violencia Trabalho em saude mental trabalho avancado","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_trabalh_violencia_trabalho"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
