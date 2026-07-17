#!/usr/bin/env python3
"""Mesolimbic Dopamine"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/mesolimbic_dopamine", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_mesolimbic_dopamine","s":"ativo","d":"Mesolimbic Dopamine","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_mesolimbic_dopamine"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
