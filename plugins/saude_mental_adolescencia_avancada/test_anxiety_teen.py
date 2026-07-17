#!/usr/bin/env python3
"""Test Anxiety Teen"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/test_anxiety_teen", tags=["saude_mental_adolescencia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_adole_test_anxiety_teen","s":"ativo","d":"Test Anxiety Teen","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_adole_test_anxiety_teen"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
