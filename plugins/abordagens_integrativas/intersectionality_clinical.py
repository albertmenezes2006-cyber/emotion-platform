#!/usr/bin/env python3
"""Intersectionality Clinical"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/intersectionality_clinical", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_intersectionality_clinica","s":"ativo","d":"Intersectionality Clinical","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_intersectionality_clinica"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
