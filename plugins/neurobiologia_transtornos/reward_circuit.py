#!/usr/bin/env python3
"""Reward Circuit"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/reward_circuit", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_reward_circuit","s":"ativo","d":"Reward Circuit","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_reward_circuit"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
