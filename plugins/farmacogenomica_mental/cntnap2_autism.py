#!/usr/bin/env python3
"""Cntnap2 Autism"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/cntnap2_autism", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_cntnap2_autism","s":"ativo","d":"Cntnap2 Autism","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_cntnap2_autism"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
