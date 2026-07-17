#!/usr/bin/env python3
"""Slc6A4 Transporter"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/slc6a4_transporter", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_slc6a4_transporter","s":"ativo","d":"Slc6A4 Transporter","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_slc6a4_transporter"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
