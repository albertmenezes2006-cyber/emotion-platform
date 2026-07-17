#!/usr/bin/env python3
"""Perspectiva Feminista Moral"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/perspectiva_feminista_moral", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_perspectiva_feminista_mor","s":"ativo","d":"Perspectiva Feminista Moral","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_perspectiva_feminista_mor"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
