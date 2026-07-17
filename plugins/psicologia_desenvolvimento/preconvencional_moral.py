#!/usr/bin/env python3
"""Preconvencional Moral"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/preconvencional_moral", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_preconvencional_moral","s":"ativo","d":"Preconvencional Moral","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_preconvencional_moral"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
