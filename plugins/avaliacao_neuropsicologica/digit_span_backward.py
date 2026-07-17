#!/usr/bin/env python3
"""Digit Span Backward"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/digit_span_backward", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_digit_span_backward","s":"ativo","d":"Digit Span Backward","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_digit_span_backward"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
