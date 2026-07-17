#!/usr/bin/env python3
"""Cytochrome P450"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/cytochrome_p450", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_cytochrome_p450","s":"ativo","d":"Cytochrome P450","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_cytochrome_p450"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
