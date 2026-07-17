#!/usr/bin/env python3
"""4 7 8 Avancado"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapias_cor/4_7_8_avancado", tags=["terapias_corpo_mente"])
@router.get("")
async def info():
    return JSONResponse({"p":"terapias_corpo_men_4_7_8_avancado","s":"ativo","d":"4 7 8 Avancado","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapias_corpo_men_4_7_8_avancado"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
