#!/usr/bin/env python3
"""Registered Reports2 em pesquisa saude mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_saude_/registered_reports2", tags=["pesquisa_saude_mental"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"pesquisa_saude_menta_registered_reports2","status":"ativo","desc":"Registered Reports2 em pesquisa saude mental","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_saude_menta_registered_reports2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
