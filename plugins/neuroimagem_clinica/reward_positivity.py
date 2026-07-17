#!/usr/bin/env python3
"""Reward Positivity"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/reward_positivity", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_reward_positivity","s":"ativo","d":"Reward Positivity","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_reward_positivity"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
