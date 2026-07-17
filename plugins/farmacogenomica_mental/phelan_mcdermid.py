#!/usr/bin/env python3
"""Phelan Mcdermid"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/phelan_mcdermid", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_phelan_mcdermid","s":"ativo","d":"Phelan Mcdermid","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_phelan_mcdermid"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
