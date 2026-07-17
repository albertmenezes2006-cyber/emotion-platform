#!/usr/bin/env python3
"""Dual Career Athletes"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/dual_career_athletes", tags=["saude_mental_esporte"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_espor_dual_career_athletes","s":"ativo","d":"Dual Career Athletes","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_espor_dual_career_athletes"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
