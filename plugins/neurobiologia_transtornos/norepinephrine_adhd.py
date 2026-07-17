#!/usr/bin/env python3
"""Norepinephrine Adhd"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/norepinephrine_adhd", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_norepinephrine_adhd","s":"ativo","d":"Norepinephrine Adhd","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_norepinephrine_adhd"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
