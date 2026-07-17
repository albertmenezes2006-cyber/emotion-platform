#!/usr/bin/env python3
"""Default Mode Adhd"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/default_mode_adhd", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_default_mode_adhd","s":"ativo","d":"Default Mode Adhd","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_default_mode_adhd"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
