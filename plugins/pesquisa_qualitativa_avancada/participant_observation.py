#!/usr/bin/env python3
"""Participant Observation"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/participant_observation", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_participant_observation","s":"ativo","d":"Participant Observation","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_participant_observation"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
