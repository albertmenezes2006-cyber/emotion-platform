#!/usr/bin/env python3
"""Juizo Moral"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/juizo_moral", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_juizo_moral","s":"ativo","d":"Juizo Moral","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_juizo_moral"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
