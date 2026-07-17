#!/usr/bin/env python3
"""Afeto Vitalidade"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/afeto_vitalidade", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_afeto_vitalidade","s":"ativo","d":"Afeto Vitalidade","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_afeto_vitalidade"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
