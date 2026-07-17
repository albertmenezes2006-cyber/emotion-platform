#!/usr/bin/env python3
"""Identidade Envelhecimento"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/identidade_envelhecimento", tags=["saude_mental_idoso_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_idoso_identidade_envelhecimento","s":"ativo","d":"Identidade Envelhecimento","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_idoso_identidade_envelhecimento"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
