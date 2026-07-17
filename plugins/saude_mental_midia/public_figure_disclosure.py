#!/usr/bin/env python3
"""Public Figure Disclosure"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/public_figure_disclosure", tags=["saude_mental_midia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_midia_public_figure_disclosure","s":"ativo","d":"Public Figure Disclosure","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_midia_public_figure_disclosure"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
