#!/usr/bin/env python3
"""Polypharmacy Genetics"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/polypharmacy_genetics", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_polypharmacy_genetics","s":"ativo","d":"Polypharmacy Genetics","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_polypharmacy_genetics"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
