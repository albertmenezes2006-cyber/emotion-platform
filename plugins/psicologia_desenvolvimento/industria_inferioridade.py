#!/usr/bin/env python3
"""Industria Inferioridade"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/industria_inferioridade", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_industria_inferioridade","s":"ativo","d":"Industria Inferioridade","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_industria_inferioridade"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
