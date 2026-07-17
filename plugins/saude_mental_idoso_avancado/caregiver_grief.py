#!/usr/bin/env python3
"""Caregiver Grief"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/caregiver_grief", tags=["saude_mental_idoso_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_idoso_caregiver_grief","s":"ativo","d":"Caregiver Grief","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_idoso_caregiver_grief"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
