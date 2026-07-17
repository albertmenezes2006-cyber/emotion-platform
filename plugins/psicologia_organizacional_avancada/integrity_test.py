#!/usr/bin/env python3
"""Integrity Test"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/integrity_test", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_integrity_test","s":"ativo","d":"Integrity Test","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_integrity_test"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
