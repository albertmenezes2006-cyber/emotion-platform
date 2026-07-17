#!/usr/bin/env python3
"""Infancia Precoce Mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/infancia_precoce_mental", tags=["saude_mental_infancia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_infan_infancia_precoce_mental","s":"ativo","d":"Infancia Precoce Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_infan_infancia_precoce_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
