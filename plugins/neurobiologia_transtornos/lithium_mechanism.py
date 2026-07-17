#!/usr/bin/env python3
"""Lithium Mechanism"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/lithium_mechanism", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_lithium_mechanism","s":"ativo","d":"Lithium Mechanism","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_lithium_mechanism"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
