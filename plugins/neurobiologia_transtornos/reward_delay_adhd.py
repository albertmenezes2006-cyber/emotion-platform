#!/usr/bin/env python3
"""Reward Delay Adhd"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/reward_delay_adhd", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_reward_delay_adhd","s":"ativo","d":"Reward Delay Adhd","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_reward_delay_adhd"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
