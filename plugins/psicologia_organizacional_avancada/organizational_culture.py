#!/usr/bin/env python3
"""Organizational Culture"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/organizational_culture", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_organizational_culture","s":"ativo","d":"Organizational Culture","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_organizational_culture"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
