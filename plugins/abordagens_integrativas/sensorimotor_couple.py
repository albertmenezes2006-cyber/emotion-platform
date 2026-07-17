#!/usr/bin/env python3
"""Sensorimotor Couple"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/sensorimotor_couple", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_sensorimotor_couple","s":"ativo","d":"Sensorimotor Couple","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_sensorimotor_couple"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
