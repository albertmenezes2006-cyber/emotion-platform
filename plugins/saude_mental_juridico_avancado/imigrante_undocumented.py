#!/usr/bin/env python3
"""Imigrante Undocumented"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/imigrante_undocumented", tags=["saude_mental_juridico_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_jurid_imigrante_undocumented","s":"ativo","d":"Imigrante Undocumented","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_jurid_imigrante_undocumented"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
