#!/usr/bin/env python3
"""Stress Memory Impairment"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/stress_memory_impairment", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_stress_memory_impairment","s":"ativo","d":"Stress Memory Impairment","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_stress_memory_impairment"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
