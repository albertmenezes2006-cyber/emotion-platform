#!/usr/bin/env python3
"""Neurobiologia Tdah"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/neurobiologia_tdah", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_neurobiologia_tdah","s":"ativo","d":"Neurobiologia Tdah","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_neurobiologia_tdah"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
