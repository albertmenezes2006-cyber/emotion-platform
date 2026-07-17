#!/usr/bin/env python3
"""Pericia Previdenciaria"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/pericia_previdenciaria", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_pericia_previdenciaria","s":"ativo","d":"Pericia Previdenciaria","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_pericia_previdenciaria"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
