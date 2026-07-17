#!/usr/bin/env python3
"""Circadian Bipolar"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/circadian_bipolar", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_circadian_bipolar","s":"ativo","d":"Circadian Bipolar","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_circadian_bipolar"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
