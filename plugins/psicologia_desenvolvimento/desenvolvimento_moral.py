#!/usr/bin/env python3
"""Desenvolvimento Moral"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/desenvolvimento_moral", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_desenvolvimento_moral","s":"ativo","d":"Desenvolvimento Moral","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_desenvolvimento_moral"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
