#!/usr/bin/env python3
"""Ventral Vagal Activation"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapias_cor/ventral_vagal_activation", tags=["terapias_corpo_mente"])
@router.get("")
async def info():
    return JSONResponse({"p":"terapias_corpo_men_ventral_vagal_activation","s":"ativo","d":"Ventral Vagal Activation","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapias_corpo_men_ventral_vagal_activation"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
