#!/usr/bin/env python3
"""Middle Ear Muscles"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapias_cor/middle_ear_muscles", tags=["terapias_corpo_mente"])
@router.get("")
async def info():
    return JSONResponse({"p":"terapias_corpo_men_middle_ear_muscles","s":"ativo","d":"Middle Ear Muscles","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapias_corpo_men_middle_ear_muscles"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
