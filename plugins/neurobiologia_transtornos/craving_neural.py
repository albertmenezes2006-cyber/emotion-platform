#!/usr/bin/env python3
"""Craving Neural"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/craving_neural", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_craving_neural","s":"ativo","d":"Craving Neural","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_craving_neural"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
