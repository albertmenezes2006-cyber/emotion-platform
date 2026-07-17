#!/usr/bin/env python3
"""Competencia Processual"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/competencia_processual", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_competencia_processual","s":"ativo","d":"Competencia Processual","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_competencia_processual"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
