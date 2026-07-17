#!/usr/bin/env python3
"""Afrocentricidade em saude mental grupos especificos"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental_gr/afrocentricidade", tags=["saude_mental_grupos_especificos"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"saude_mental_grupos__afrocentricidade","status":"ativo","desc":"Afrocentricidade em saude mental grupos especificos","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_grupos__afrocentricidade"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
