#!/usr/bin/env python3
"""Nutrition Child Mental2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/nutrition_child_mental2", tags=["saude_mental_infancia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_infan_nutrition_child_mental2","s":"ativo","d":"Nutrition Child Mental2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_infan_nutrition_child_mental2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
