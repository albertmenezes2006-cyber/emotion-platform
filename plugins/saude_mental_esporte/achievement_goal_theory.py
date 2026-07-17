#!/usr/bin/env python3
"""Achievement Goal Theory"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/achievement_goal_theory", tags=["saude_mental_esporte"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_espor_achievement_goal_theory","s":"ativo","d":"Achievement Goal Theory","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_espor_achievement_goal_theory"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
