#!/usr/bin/env python3
"""Protection Order Psychology"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/protection_order_psychology", tags=["saude_mental_juridico_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_jurid_protection_order_psycholo","s":"ativo","d":"Protection Order Psychology","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_jurid_protection_order_psycholo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
