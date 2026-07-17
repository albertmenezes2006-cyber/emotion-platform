#!/usr/bin/env python3
"""Extrinsic Motivation"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/extrinsic_motivation", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_extrinsic_motivation","s":"ativo","d":"Extrinsic Motivation","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_extrinsic_motivation"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
