#!/usr/bin/env python3
"""Mesocortical Dopamine"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/mesocortical_dopamine", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_mesocortical_dopamine","s":"ativo","d":"Mesocortical Dopamine","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_mesocortical_dopamine"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
