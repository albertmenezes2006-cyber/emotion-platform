#!/usr/bin/env python3
"""Reward Prediction Error"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/reward_prediction_error", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_reward_prediction_error","s":"ativo","d":"Reward Prediction Error","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_reward_prediction_error"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
