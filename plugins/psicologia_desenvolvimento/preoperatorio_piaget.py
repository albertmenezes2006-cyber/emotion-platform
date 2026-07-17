#!/usr/bin/env python3
"""Preoperatorio Piaget"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/preoperatorio_piaget", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_preoperatorio_piaget","s":"ativo","d":"Preoperatorio Piaget","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_preoperatorio_piaget"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
