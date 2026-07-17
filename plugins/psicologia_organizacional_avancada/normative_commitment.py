#!/usr/bin/env python3
"""Normative Commitment"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/normative_commitment", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_normative_commitment","s":"ativo","d":"Normative Commitment","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_normative_commitment"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
