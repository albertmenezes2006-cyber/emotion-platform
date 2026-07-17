#!/usr/bin/env python3
"""Non Coding Rna"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/non_coding_rna", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_non_coding_rna","s":"ativo","d":"Non Coding Rna","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_non_coding_rna"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
