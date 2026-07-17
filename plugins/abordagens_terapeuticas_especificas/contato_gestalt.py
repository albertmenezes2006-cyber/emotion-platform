#!/usr/bin/env python3
"""Contato Gestalt em abordagens terapeuticas especificas"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_tera/contato_gestalt", tags=["abordagens_terapeuticas_especificas"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"abordagens_terapeuti_contato_gestalt","status":"ativo","desc":"Contato Gestalt em abordagens terapeuticas especificas","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_terapeuti_contato_gestalt"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
