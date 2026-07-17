#!/usr/bin/env python3
"""Inner Critic Self Compassion"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/inner_critic_self_compassion", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_inner_critic_self_compass","s":"ativo","d":"Inner Critic Self Compassion","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_inner_critic_self_compass"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
