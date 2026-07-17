#!/usr/bin/env python3
"""Zona Desenvolvimento Proximal"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/zona_desenvolvimento_proxima", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_zona_desenvolvimento_prox","s":"ativo","d":"Zona Desenvolvimento Proximal","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_zona_desenvolvimento_prox"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
