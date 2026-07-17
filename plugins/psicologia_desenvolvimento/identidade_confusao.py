#!/usr/bin/env python3
"""Identidade Confusao"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/identidade_confusao", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_identidade_confusao","s":"ativo","d":"Identidade Confusao","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_identidade_confusao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
