#!/usr/bin/env python3
"""Machiavellianism Leader"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/machiavellianism_leader", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_machiavellianism_leader","s":"ativo","d":"Machiavellianism Leader","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_machiavellianism_leader"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
