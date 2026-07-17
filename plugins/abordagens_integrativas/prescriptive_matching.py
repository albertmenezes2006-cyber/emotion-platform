#!/usr/bin/env python3
"""Prescriptive Matching"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/prescriptive_matching", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_prescriptive_matching","s":"ativo","d":"Prescriptive Matching","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_prescriptive_matching"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
