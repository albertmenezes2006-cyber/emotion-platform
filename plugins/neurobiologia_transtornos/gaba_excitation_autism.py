#!/usr/bin/env python3
"""Gaba Excitation Autism"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/gaba_excitation_autism", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_gaba_excitation_autism","s":"ativo","d":"Gaba Excitation Autism","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_gaba_excitation_autism"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
