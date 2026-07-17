#!/usr/bin/env python3
"""Suicide Prevention Military"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/suicide_prevention_military", tags=["saude_mental_militar"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_milit_suicide_prevention_milita","s":"ativo","d":"Suicide Prevention Military","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_milit_suicide_prevention_milita"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
