#!/usr/bin/env python3
"""Distributed Teams"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/distributed_teams", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_distributed_teams","s":"ativo","d":"Distributed Teams","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_distributed_teams"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
