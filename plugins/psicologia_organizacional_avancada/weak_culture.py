#!/usr/bin/env python3
"""Weak Culture"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/weak_culture", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_weak_culture","s":"ativo","d":"Weak Culture","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_weak_culture"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
