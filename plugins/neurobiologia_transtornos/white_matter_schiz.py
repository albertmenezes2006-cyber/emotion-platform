#!/usr/bin/env python3
"""White Matter Schiz"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/white_matter_schiz", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_white_matter_schiz","s":"ativo","d":"White Matter Schiz","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_white_matter_schiz"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
