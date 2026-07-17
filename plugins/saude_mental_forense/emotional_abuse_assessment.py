#!/usr/bin/env python3
"""Emotional Abuse Assessment"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/emotional_abuse_assessment", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_emotional_abuse_assessmen","s":"ativo","d":"Emotional Abuse Assessment","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_emotional_abuse_assessmen"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
