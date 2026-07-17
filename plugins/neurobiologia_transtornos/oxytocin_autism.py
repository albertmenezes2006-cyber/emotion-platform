#!/usr/bin/env python3
"""Oxytocin Autism"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/oxytocin_autism", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_oxytocin_autism","s":"ativo","d":"Oxytocin Autism","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_oxytocin_autism"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
