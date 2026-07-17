#!/usr/bin/env python3
"""Intergroup Contact"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/intergroup_contact", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__intergroup_contact","s":"ativo","d":"Intergroup Contact","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__intergroup_contact"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
