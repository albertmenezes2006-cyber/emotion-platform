#!/usr/bin/env python3
"""Float Anxiety"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapias_cor/float_anxiety", tags=["terapias_corpo_mente"])
@router.get("")
async def info():
    return JSONResponse({"p":"terapias_corpo_men_float_anxiety","s":"ativo","d":"Float Anxiety","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapias_corpo_men_float_anxiety"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
