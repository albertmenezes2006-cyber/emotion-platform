#!/usr/bin/env python3
"""Creativity Tests"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/creativity_tests", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_creativity_tests","s":"ativo","d":"Creativity Tests","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_creativity_tests"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
