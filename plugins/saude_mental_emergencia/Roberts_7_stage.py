#!/usr/bin/env python3
"""Roberts 7 Stage"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/Roberts_7_stage", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_Roberts_7_stage","s":"ativo","d":"Roberts 7 Stage","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_Roberts_7_stage"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
