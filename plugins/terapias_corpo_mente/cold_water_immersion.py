#!/usr/bin/env python3
"""Cold Water Immersion"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapias_cor/cold_water_immersion", tags=["terapias_corpo_mente"])
@router.get("")
async def info():
    return JSONResponse({"p":"terapias_corpo_men_cold_water_immersion","s":"ativo","d":"Cold Water Immersion","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapias_corpo_men_cold_water_immersion"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
