#!/usr/bin/env python3
"""Allostatic Load"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/allostatic_load", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_allostatic_load","s":"ativo","d":"Allostatic Load","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_allostatic_load"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
