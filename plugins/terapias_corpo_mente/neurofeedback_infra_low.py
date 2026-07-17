#!/usr/bin/env python3
"""Neurofeedback Infra Low"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapias_cor/neurofeedback_infra_low", tags=["terapias_corpo_mente"])
@router.get("")
async def info():
    return JSONResponse({"p":"terapias_corpo_men_neurofeedback_infra_low","s":"ativo","d":"Neurofeedback Infra Low","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapias_corpo_men_neurofeedback_infra_low"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
