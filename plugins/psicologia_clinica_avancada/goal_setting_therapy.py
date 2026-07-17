#!/usr/bin/env python3
"""Goal Setting Therapy"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/goal_setting_therapy", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_goal_setting_therapy","s":"ativo","d":"Goal Setting Therapy","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_goal_setting_therapy"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
