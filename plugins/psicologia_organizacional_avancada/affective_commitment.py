#!/usr/bin/env python3
"""Affective Commitment"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/affective_commitment", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_affective_commitment","s":"ativo","d":"Affective Commitment","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_affective_commitment"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
