#!/usr/bin/env python3
"""Mensagem Framing"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/mensagem_framing", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__mensagem_framing","s":"ativo","d":"Mensagem Framing","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__mensagem_framing"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
