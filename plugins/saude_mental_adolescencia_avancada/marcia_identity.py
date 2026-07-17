#!/usr/bin/env python3
"""Marcia Identity"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/marcia_identity", tags=["saude_mental_adolescencia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_adole_marcia_identity","s":"ativo","d":"Marcia Identity","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_adole_marcia_identity"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
