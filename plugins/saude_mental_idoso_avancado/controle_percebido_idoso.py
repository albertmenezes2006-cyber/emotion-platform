#!/usr/bin/env python3
"""Controle Percebido Idoso"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/controle_percebido_idoso", tags=["saude_mental_idoso_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_idoso_controle_percebido_idoso","s":"ativo","d":"Controle Percebido Idoso","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_idoso_controle_percebido_idoso"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
