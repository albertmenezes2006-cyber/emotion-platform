#!/usr/bin/env python3
"""Vascular Depression"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/vascular_depression", tags=["saude_mental_idoso_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_idoso_vascular_depression","s":"ativo","d":"Vascular Depression","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_idoso_vascular_depression"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
