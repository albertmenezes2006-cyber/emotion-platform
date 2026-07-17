#!/usr/bin/env python3
"""Positive Aging2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/positive_aging2", tags=["saude_mental_idoso_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_idoso_positive_aging2","s":"ativo","d":"Positive Aging2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_idoso_positive_aging2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
