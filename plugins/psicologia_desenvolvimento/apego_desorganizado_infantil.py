#!/usr/bin/env python3
"""Apego Desorganizado Infantil"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/apego_desorganizado_infantil", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_apego_desorganizado_infan","s":"ativo","d":"Apego Desorganizado Infantil","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_apego_desorganizado_infan"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
