#!/usr/bin/env python3
"""Negative Response Bias"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/negative_response_bias", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_negative_response_bias","s":"ativo","d":"Negative Response Bias","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_negative_response_bias"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
