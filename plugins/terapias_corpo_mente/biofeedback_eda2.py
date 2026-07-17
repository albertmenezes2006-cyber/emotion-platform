#!/usr/bin/env python3
"""Biofeedback Eda2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapias_cor/biofeedback_eda2", tags=["terapias_corpo_mente"])
@router.get("")
async def info():
    return JSONResponse({"p":"terapias_corpo_men_biofeedback_eda2","s":"ativo","d":"Biofeedback Eda2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapias_corpo_men_biofeedback_eda2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
