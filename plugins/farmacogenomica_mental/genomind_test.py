#!/usr/bin/env python3
"""Genomind Test"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/genomind_test", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_genomind_test","s":"ativo","d":"Genomind Test","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_genomind_test"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
