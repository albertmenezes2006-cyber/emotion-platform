#!/usr/bin/env python3
"""Dopamine Depression"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/dopamine_depression", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_dopamine_depression","s":"ativo","d":"Dopamine Depression","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_dopamine_depression"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
