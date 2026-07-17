#!/usr/bin/env python3
"""Phallometric Testing"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/phallometric_testing", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_phallometric_testing","s":"ativo","d":"Phallometric Testing","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_phallometric_testing"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
