#!/usr/bin/env python3
"""Dual Attention Stimulus"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapias_cor/dual_attention_stimulus", tags=["terapias_corpo_mente"])
@router.get("")
async def info():
    return JSONResponse({"p":"terapias_corpo_men_dual_attention_stimulus","s":"ativo","d":"Dual Attention Stimulus","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapias_corpo_men_dual_attention_stimulus"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
