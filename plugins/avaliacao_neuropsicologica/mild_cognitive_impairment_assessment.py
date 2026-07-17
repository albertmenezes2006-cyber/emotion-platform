#!/usr/bin/env python3
"""Mild Cognitive Impairment Assessment"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/mild_cognitive_impairment_as", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_mild_cognitive_impairment","s":"ativo","d":"Mild Cognitive Impairment Assessment","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_mild_cognitive_impairment"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
