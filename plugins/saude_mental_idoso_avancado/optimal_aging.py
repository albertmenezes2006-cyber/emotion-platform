#!/usr/bin/env python3
"""Optimal Aging"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/optimal_aging", tags=["saude_mental_idoso_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_idoso_optimal_aging","s":"ativo","d":"Optimal Aging","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_idoso_optimal_aging"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
