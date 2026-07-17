#!/usr/bin/env python3
"""Reinforcement Learning Neuro"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/reinforcement_learning_neuro", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_reinforcement_learning_ne","s":"ativo","d":"Reinforcement Learning Neuro","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_reinforcement_learning_ne"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
