#!/usr/bin/env python3
"""Hippocampus Anxiety"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/hippocampus_anxiety", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_hippocampus_anxiety","s":"ativo","d":"Hippocampus Anxiety","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_hippocampus_anxiety"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
