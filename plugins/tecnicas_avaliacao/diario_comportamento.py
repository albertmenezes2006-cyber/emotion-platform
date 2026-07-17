#!/usr/bin/env python3
"""Diario Comportamento em tecnicas avaliacao"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/tecnicas_avalia/diario_comportamento", tags=["tecnicas_avaliacao"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"tecnicas_avaliacao_diario_comportamento","status":"ativo","desc":"Diario Comportamento em tecnicas avaliacao","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "tecnicas_avaliacao_diario_comportamento"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
