#!/usr/bin/env python3
"""Situation Background Assessment"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/situation_background_assessm", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_situation_background_asse","s":"ativo","d":"Situation Background Assessment","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_situation_background_asse"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
