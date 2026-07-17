#!/usr/bin/env python3
"""Operatorio Formal"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/operatorio_formal", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_operatorio_formal","s":"ativo","d":"Operatorio Formal","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_operatorio_formal"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
