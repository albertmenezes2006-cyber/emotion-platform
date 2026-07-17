#!/usr/bin/env python3
"""Convencional Moral"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/convencional_moral", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_convencional_moral","s":"ativo","d":"Convencional Moral","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_convencional_moral"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
