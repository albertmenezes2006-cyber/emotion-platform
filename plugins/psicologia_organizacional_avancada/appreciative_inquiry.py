#!/usr/bin/env python3
"""Appreciative Inquiry"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/appreciative_inquiry", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_appreciative_inquiry","s":"ativo","d":"Appreciative Inquiry","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_appreciative_inquiry"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
