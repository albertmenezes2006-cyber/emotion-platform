#!/usr/bin/env python3
"""Separacao Familiar Fronteira"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/separacao_familiar_fronteira", tags=["saude_mental_juridico_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_jurid_separacao_familiar_fronte","s":"ativo","d":"Separacao Familiar Fronteira","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_jurid_separacao_familiar_fronte"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
