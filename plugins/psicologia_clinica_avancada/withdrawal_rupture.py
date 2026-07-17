#!/usr/bin/env python3
"""Withdrawal Rupture"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/withdrawal_rupture", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_withdrawal_rupture","s":"ativo","d":"Withdrawal Rupture","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_withdrawal_rupture"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
