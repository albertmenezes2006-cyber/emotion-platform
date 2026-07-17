#!/usr/bin/env python3
"""Planning Battery"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/planning_battery", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_planning_battery","s":"ativo","d":"Planning Battery","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_planning_battery"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
