#!/usr/bin/env python3
"""Extrinsic Motivation Sport"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/extrinsic_motivation_sport", tags=["saude_mental_esporte"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_espor_extrinsic_motivation_spor","s":"ativo","d":"Extrinsic Motivation Sport","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_espor_extrinsic_motivation_spor"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
