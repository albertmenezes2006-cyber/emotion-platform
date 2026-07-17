#!/usr/bin/env python3
"""Float Rest Tank"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapias_cor/float_rest_tank", tags=["terapias_corpo_mente"])
@router.get("")
async def info():
    return JSONResponse({"p":"terapias_corpo_men_float_rest_tank","s":"ativo","d":"Float Rest Tank","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapias_corpo_men_float_rest_tank"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
