#!/usr/bin/env python3
"""Operatorio Concreto"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/operatorio_concreto", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_operatorio_concreto","s":"ativo","d":"Operatorio Concreto","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_operatorio_concreto"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
