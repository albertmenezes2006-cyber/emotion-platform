#!/usr/bin/env python3
"""Safer Model"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/SAFER_model", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_SAFER_model","s":"ativo","d":"Safer Model","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_SAFER_model"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
