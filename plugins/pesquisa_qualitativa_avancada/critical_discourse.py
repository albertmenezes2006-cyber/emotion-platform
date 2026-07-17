#!/usr/bin/env python3
"""Critical Discourse"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/critical_discourse", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_critical_discourse","s":"ativo","d":"Critical Discourse","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_critical_discourse"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
