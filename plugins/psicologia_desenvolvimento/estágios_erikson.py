#!/usr/bin/env python3
"""Estágios Erikson"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/estágios_erikson", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_estágios_erikson","s":"ativo","d":"Estágios Erikson","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_estágios_erikson"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
