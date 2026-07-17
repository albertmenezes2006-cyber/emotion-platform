#!/usr/bin/env python3
"""Paul Therapy Question"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/paul_therapy_question", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_paul_therapy_question","s":"ativo","d":"Paul Therapy Question","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_paul_therapy_question"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
