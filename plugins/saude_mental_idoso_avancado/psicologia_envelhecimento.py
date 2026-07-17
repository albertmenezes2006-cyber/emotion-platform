#!/usr/bin/env python3
"""Psicologia Envelhecimento"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/psicologia_envelhecimento", tags=["saude_mental_idoso_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_idoso_psicologia_envelhecimento","s":"ativo","d":"Psicologia Envelhecimento","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_idoso_psicologia_envelhecimento"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
