#!/usr/bin/env python3
"""Design Fluency"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/design_fluency", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_design_fluency","s":"ativo","d":"Design Fluency","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_design_fluency"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
