#!/usr/bin/env python3
"""Confianca Desconfianca"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/confianca_desconfianca", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_confianca_desconfianca","s":"ativo","d":"Confianca Desconfianca","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_confianca_desconfianca"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
