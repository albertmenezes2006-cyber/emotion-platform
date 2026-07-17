#!/usr/bin/env python3
"""Collaborative Assessment"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/collaborative_assessment", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_collaborative_assessment","s":"ativo","d":"Collaborative Assessment","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_collaborative_assessment"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
