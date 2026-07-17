#!/usr/bin/env python3
"""Domestic Violence Risk"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/domestic_violence_risk", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_domestic_violence_risk","s":"ativo","d":"Domestic Violence Risk","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_domestic_violence_risk"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
