#!/usr/bin/env python3
"""Memory Reconsolidation Court"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/memory_reconsolidation_court", tags=["saude_mental_juridico_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_jurid_memory_reconsolidation_co","s":"ativo","d":"Memory Reconsolidation Court","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_jurid_memory_reconsolidation_co"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
