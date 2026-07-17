#!/usr/bin/env python3
"""Dc 0 5 Classification"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/DC_0_5_classification", tags=["saude_mental_infancia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_infan_DC_0_5_classification","s":"ativo","d":"Dc 0 5 Classification","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_infan_DC_0_5_classification"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
