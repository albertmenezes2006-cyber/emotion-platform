#!/usr/bin/env python3
"""Neuroception Safety"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapias_cor/neuroception_safety", tags=["terapias_corpo_mente"])
@router.get("")
async def info():
    return JSONResponse({"p":"terapias_corpo_men_neuroception_safety","s":"ativo","d":"Neuroception Safety","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapias_corpo_men_neuroception_safety"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
