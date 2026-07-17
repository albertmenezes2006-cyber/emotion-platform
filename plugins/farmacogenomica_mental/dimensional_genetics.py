#!/usr/bin/env python3
"""Dimensional Genetics"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/dimensional_genetics", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_dimensional_genetics","s":"ativo","d":"Dimensional Genetics","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_dimensional_genetics"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
