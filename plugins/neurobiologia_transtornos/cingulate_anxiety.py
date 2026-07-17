#!/usr/bin/env python3
"""Cingulate Anxiety"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/cingulate_anxiety", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_cingulate_anxiety","s":"ativo","d":"Cingulate Anxiety","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_cingulate_anxiety"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
