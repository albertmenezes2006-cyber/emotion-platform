#!/usr/bin/env python3
"""Central Peripheral Route"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/central_peripheral_route", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__central_peripheral_route","s":"ativo","d":"Central Peripheral Route","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__central_peripheral_route"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
