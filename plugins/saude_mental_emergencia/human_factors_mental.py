#!/usr/bin/env python3
"""Human Factors Mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/human_factors_mental", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_human_factors_mental","s":"ativo","d":"Human Factors Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_human_factors_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
