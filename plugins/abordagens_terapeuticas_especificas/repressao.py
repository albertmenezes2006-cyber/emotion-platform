#!/usr/bin/env python3
"""Repressao em abordagens terapeuticas especificas"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_tera/repressao", tags=["abordagens_terapeuticas_especificas"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"abordagens_terapeuti_repressao","status":"ativo","desc":"Repressao em abordagens terapeuticas especificas","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_terapeuti_repressao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
