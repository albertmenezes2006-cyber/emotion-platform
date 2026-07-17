#!/usr/bin/env python3
"""Protein Binding"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/protein_binding", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_protein_binding","s":"ativo","d":"Protein Binding","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_protein_binding"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
