#!/usr/bin/env python3
"""Valproate Mechanism"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/valproate_mechanism", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_valproate_mechanism","s":"ativo","d":"Valproate Mechanism","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_valproate_mechanism"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
