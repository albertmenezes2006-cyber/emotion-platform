#!/usr/bin/env python3
"""Wim Hof Avancado"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapias_cor/wim_hof_avancado", tags=["terapias_corpo_mente"])
@router.get("")
async def info():
    return JSONResponse({"p":"terapias_corpo_men_wim_hof_avancado","s":"ativo","d":"Wim Hof Avancado","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapias_corpo_men_wim_hof_avancado"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
