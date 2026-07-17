#!/usr/bin/env python3
"""Hipnose Habitos em abordagens terapeuticas especificas"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_tera/hipnose_habitos", tags=["abordagens_terapeuticas_especificas"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"abordagens_terapeuti_hipnose_habitos","status":"ativo","desc":"Hipnose Habitos em abordagens terapeuticas especificas","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_terapeuti_hipnose_habitos"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
