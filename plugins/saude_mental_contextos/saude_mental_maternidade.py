#!/usr/bin/env python3
"""Saude Mental Maternidade em saude mental contextos"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental_co/saude_mental_maternidade", tags=["saude_mental_contextos"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"saude_mental_context_saude_mental_maternidade","status":"ativo","desc":"Saude Mental Maternidade em saude mental contextos","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_context_saude_mental_maternidade"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
