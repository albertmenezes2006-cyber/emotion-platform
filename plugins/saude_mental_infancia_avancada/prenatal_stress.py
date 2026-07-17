#!/usr/bin/env python3
"""Prenatal Stress"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/prenatal_stress", tags=["saude_mental_infancia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_infan_prenatal_stress","s":"ativo","d":"Prenatal Stress","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_infan_prenatal_stress"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
