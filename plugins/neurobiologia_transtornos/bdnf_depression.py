#!/usr/bin/env python3
"""Bdnf Depression"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/bdnf_depression", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_bdnf_depression","s":"ativo","d":"Bdnf Depression","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_bdnf_depression"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
