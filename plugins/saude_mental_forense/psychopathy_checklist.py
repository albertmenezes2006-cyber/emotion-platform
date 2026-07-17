#!/usr/bin/env python3
"""Psychopathy Checklist"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/psychopathy_checklist", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_psychopathy_checklist","s":"ativo","d":"Psychopathy Checklist","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_psychopathy_checklist"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
