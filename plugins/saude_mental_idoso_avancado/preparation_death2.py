#!/usr/bin/env python3
"""Preparation Death2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/preparation_death2", tags=["saude_mental_idoso_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_idoso_preparation_death2","s":"ativo","d":"Preparation Death2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_idoso_preparation_death2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
