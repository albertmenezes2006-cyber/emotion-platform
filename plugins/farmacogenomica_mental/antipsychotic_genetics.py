#!/usr/bin/env python3
"""Antipsychotic Genetics"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/antipsychotic_genetics", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_antipsychotic_genetics","s":"ativo","d":"Antipsychotic Genetics","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_antipsychotic_genetics"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
