#!/usr/bin/env python3
"""Turn Taking"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/turn_taking", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_turn_taking","s":"ativo","d":"Turn Taking","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_turn_taking"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
