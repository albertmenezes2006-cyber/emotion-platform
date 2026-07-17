#!/usr/bin/env python3
"""Antipsychotic Mech"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/antipsychotic_mech", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_antipsychotic_mech","s":"ativo","d":"Antipsychotic Mech","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_antipsychotic_mech"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
