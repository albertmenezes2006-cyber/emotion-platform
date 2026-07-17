#!/usr/bin/env python3
"""Preschool Mental Health"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/preschool_mental_health", tags=["saude_mental_infancia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_infan_preschool_mental_health","s":"ativo","d":"Preschool Mental Health","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_infan_preschool_mental_health"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
