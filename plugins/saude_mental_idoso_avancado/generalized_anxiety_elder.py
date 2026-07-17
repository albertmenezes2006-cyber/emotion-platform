#!/usr/bin/env python3
"""Generalized Anxiety Elder"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/generalized_anxiety_elder", tags=["saude_mental_idoso_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_idoso_generalized_anxiety_elder","s":"ativo","d":"Generalized Anxiety Elder","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_idoso_generalized_anxiety_elder"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
