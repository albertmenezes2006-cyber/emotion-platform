#!/usr/bin/env python3
"""Disordered Eating Teen"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/disordered_eating_teen", tags=["saude_mental_adolescencia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_adole_disordered_eating_teen","s":"ativo","d":"Disordered Eating Teen","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_adole_disordered_eating_teen"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
