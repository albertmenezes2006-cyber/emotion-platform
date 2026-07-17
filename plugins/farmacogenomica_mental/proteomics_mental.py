#!/usr/bin/env python3
"""Proteomics Mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/proteomics_mental", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_proteomics_mental","s":"ativo","d":"Proteomics Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_proteomics_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
