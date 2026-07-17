#!/usr/bin/env python3
"""Outpatient Commitment"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/outpatient_commitment", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_outpatient_commitment","s":"ativo","d":"Outpatient Commitment","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_outpatient_commitment"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
