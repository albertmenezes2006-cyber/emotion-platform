#!/usr/bin/env python3
"""Spr Inf"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/spr_inf", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_spr_inf","s":"ativo","d":"Spr Inf","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_spr_inf"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
