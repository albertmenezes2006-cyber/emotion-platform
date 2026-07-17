#!/usr/bin/env python3
"""Commitment Organizational"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/commitment_organizational", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_commitment_organizational","s":"ativo","d":"Commitment Organizational","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_commitment_organizational"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
