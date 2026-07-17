#!/usr/bin/env python3
"""Neuropeptides"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/neuropeptides", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_neuropeptides","s":"ativo","d":"Neuropeptides","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_neuropeptides"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
