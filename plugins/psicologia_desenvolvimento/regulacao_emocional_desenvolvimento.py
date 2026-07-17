#!/usr/bin/env python3
"""Regulacao Emocional Desenvolvimento"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/regulacao_emocional_desenvol", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_regulacao_emocional_desen","s":"ativo","d":"Regulacao Emocional Desenvolvimento","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_regulacao_emocional_desen"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
