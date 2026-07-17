#!/usr/bin/env python3
"""Prefrontal Anxiety"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/prefrontal_anxiety", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_prefrontal_anxiety","s":"ativo","d":"Prefrontal Anxiety","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_prefrontal_anxiety"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
