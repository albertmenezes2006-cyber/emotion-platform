#!/usr/bin/env python3
"""Perspectiva Taking"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/perspectiva_taking", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_perspectiva_taking","s":"ativo","d":"Perspectiva Taking","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_perspectiva_taking"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
