#!/usr/bin/env python3
"""Acceptance Commitment Adv"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/acceptance_commitment_adv", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_acceptance_commitment_adv","s":"ativo","d":"Acceptance Commitment Adv","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_acceptance_commitment_adv"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
