#!/usr/bin/env python3
"""Nucleus Accumbens"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/nucleus_accumbens", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_nucleus_accumbens","s":"ativo","d":"Nucleus Accumbens","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_nucleus_accumbens"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
