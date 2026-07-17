#!/usr/bin/env python3
"""Scaffolding Vygotsky"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/scaffolding_vygotsky", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_scaffolding_vygotsky","s":"ativo","d":"Scaffolding Vygotsky","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_scaffolding_vygotsky"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
