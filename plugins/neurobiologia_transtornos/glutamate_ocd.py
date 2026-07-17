#!/usr/bin/env python3
"""Glutamate Ocd"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/glutamate_ocd", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_glutamate_ocd","s":"ativo","d":"Glutamate Ocd","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_glutamate_ocd"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
