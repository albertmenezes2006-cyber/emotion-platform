#!/usr/bin/env python3
"""Refugiado Asylum Mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/refugiado_asylum_mental", tags=["saude_mental_juridico_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_jurid_refugiado_asylum_mental","s":"ativo","d":"Refugiado Asylum Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_jurid_refugiado_asylum_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
