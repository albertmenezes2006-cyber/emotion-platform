#!/usr/bin/env python3
"""Cold Shower Protocol"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapias_cor/cold_shower_protocol", tags=["terapias_corpo_mente"])
@router.get("")
async def info():
    return JSONResponse({"p":"terapias_corpo_men_cold_shower_protocol","s":"ativo","d":"Cold Shower Protocol","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapias_corpo_men_cold_shower_protocol"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
