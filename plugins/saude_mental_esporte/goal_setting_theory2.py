#!/usr/bin/env python3
"""Goal Setting Theory2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/goal_setting_theory2", tags=["saude_mental_esporte"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_espor_goal_setting_theory2","s":"ativo","d":"Goal Setting Theory2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_espor_goal_setting_theory2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
