#!/usr/bin/env python3
"""Cognitive Assessment Elder"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/cognitive_assessment_elder", tags=["saude_mental_idoso_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_idoso_cognitive_assessment_elde","s":"ativo","d":"Cognitive Assessment Elder","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_idoso_cognitive_assessment_elde"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
