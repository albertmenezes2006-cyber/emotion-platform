#!/usr/bin/env python3
"""Weapon Focus"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/weapon_focus", tags=["saude_mental_juridico_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_jurid_weapon_focus","s":"ativo","d":"Weapon Focus","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_jurid_weapon_focus"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
