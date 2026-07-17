#!/usr/bin/env python3
"""Figura Fundo2 em abordagens terapeuticas especificas"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_tera/figura_fundo2", tags=["abordagens_terapeuticas_especificas"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"abordagens_terapeuti_figura_fundo2","status":"ativo","desc":"Figura Fundo2 em abordagens terapeuticas especificas","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_terapeuti_figura_fundo2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
