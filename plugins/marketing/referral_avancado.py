#!/usr/bin/env python3
"""Referral avançado v2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/ref-v2", tags=["referral_av"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "referral_av", "status": "ativo",
                          "descricao": "Referral avançado v2",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "referral_av"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
