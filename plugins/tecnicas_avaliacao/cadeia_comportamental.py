#!/usr/bin/env python3
"""Cadeia Comportamental em tecnicas avaliacao"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/tecnicas_avalia/cadeia_comportamental", tags=["tecnicas_avaliacao"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"tecnicas_avaliacao_cadeia_comportamental","status":"ativo","desc":"Cadeia Comportamental em tecnicas avaliacao","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "tecnicas_avaliacao_cadeia_comportamental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
