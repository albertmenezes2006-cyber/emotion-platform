#!/usr/bin/env python3
"""Serotonin Anxiety"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/serotonin_anxiety", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_serotonin_anxiety","s":"ativo","d":"Serotonin Anxiety","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_serotonin_anxiety"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
