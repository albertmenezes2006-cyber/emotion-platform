#!/usr/bin/env python3
"""Manifest Content"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/manifest_content", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_manifest_content","s":"ativo","d":"Manifest Content","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_manifest_content"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
