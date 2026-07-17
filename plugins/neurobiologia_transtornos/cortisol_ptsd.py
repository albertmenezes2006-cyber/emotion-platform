#!/usr/bin/env python3
"""Cortisol Ptsd"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/cortisol_ptsd", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_cortisol_ptsd","s":"ativo","d":"Cortisol Ptsd","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_cortisol_ptsd"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
