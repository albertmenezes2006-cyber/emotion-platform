#!/usr/bin/env python3
"""Abusive Supervision"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/abusive_supervision", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_abusive_supervision","s":"ativo","d":"Abusive Supervision","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_abusive_supervision"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
