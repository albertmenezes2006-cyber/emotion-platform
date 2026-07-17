#!/usr/bin/env python3
"""Sentido Si Emergente"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/sentido_si_emergente", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_sentido_si_emergente","s":"ativo","d":"Sentido Si Emergente","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_sentido_si_emergente"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
