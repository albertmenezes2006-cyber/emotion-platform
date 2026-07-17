#!/usr/bin/env python3
"""Sleep Depression Neuro"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/sleep_depression_neuro", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_sleep_depression_neuro","s":"ativo","d":"Sleep Depression Neuro","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_sleep_depression_neuro"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
