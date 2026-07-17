#!/usr/bin/env python3
"""Geratividade Estagnacao"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/geratividade_estagnacao", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_geratividade_estagnacao","s":"ativo","d":"Geratividade Estagnacao","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_geratividade_estagnacao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
