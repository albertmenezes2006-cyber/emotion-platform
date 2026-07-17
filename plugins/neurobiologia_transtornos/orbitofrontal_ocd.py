#!/usr/bin/env python3
"""Orbitofrontal Ocd"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/orbitofrontal_ocd", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_orbitofrontal_ocd","s":"ativo","d":"Orbitofrontal Ocd","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_orbitofrontal_ocd"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
