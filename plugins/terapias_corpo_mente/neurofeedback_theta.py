#!/usr/bin/env python3
"""Neurofeedback Theta"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapias_cor/neurofeedback_theta", tags=["terapias_corpo_mente"])
@router.get("")
async def info():
    return JSONResponse({"p":"terapias_corpo_men_neurofeedback_theta","s":"ativo","d":"Neurofeedback Theta","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapias_corpo_men_neurofeedback_theta"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
