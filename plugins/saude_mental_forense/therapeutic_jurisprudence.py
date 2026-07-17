#!/usr/bin/env python3
"""Therapeutic Jurisprudence"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/therapeutic_jurisprudence", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_therapeutic_jurisprudence","s":"ativo","d":"Therapeutic Jurisprudence","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_therapeutic_jurisprudence"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
