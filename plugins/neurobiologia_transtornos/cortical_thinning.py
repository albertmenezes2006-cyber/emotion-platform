#!/usr/bin/env python3
"""Cortical Thinning"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/cortical_thinning", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_cortical_thinning","s":"ativo","d":"Cortical Thinning","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_cortical_thinning"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
