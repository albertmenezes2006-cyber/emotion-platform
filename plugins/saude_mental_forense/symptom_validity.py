#!/usr/bin/env python3
"""Symptom Validity"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/symptom_validity", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_symptom_validity","s":"ativo","d":"Symptom Validity","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_symptom_validity"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
