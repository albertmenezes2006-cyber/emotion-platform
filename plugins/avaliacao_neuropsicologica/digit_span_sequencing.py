#!/usr/bin/env python3
"""Digit Span Sequencing"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/digit_span_sequencing", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_digit_span_sequencing","s":"ativo","d":"Digit Span Sequencing","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_digit_span_sequencing"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
