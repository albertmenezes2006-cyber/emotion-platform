#!/usr/bin/env python3
"""Eating Disorders Differential"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/eating_disorders_differentia", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_eating_disorders_differen","s":"ativo","d":"Eating Disorders Differential","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_eating_disorders_differen"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
