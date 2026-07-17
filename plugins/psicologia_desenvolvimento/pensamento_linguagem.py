#!/usr/bin/env python3
"""Pensamento Linguagem"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/pensamento_linguagem", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_pensamento_linguagem","s":"ativo","d":"Pensamento Linguagem","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_pensamento_linguagem"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
