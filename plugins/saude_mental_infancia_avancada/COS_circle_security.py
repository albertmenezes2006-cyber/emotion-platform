#!/usr/bin/env python3
"""Cos Circle Security"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/COS_circle_security", tags=["saude_mental_infancia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_infan_COS_circle_security","s":"ativo","d":"Cos Circle Security","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_infan_COS_circle_security"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
