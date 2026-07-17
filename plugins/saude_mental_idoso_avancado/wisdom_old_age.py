#!/usr/bin/env python3
"""Wisdom Old Age"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/wisdom_old_age", tags=["saude_mental_idoso_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_idoso_wisdom_old_age","s":"ativo","d":"Wisdom Old Age","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_idoso_wisdom_old_age"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
