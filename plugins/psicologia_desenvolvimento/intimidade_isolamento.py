#!/usr/bin/env python3
"""Intimidade Isolamento"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/intimidade_isolamento", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_intimidade_isolamento","s":"ativo","d":"Intimidade Isolamento","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_intimidade_isolamento"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
