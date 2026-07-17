#!/usr/bin/env python3
"""Maoa Maob"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/maoa_maob", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_maoa_maob","s":"ativo","d":"Maoa Maob","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_maoa_maob"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
