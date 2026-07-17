#!/usr/bin/env python3
"""Dropout Prevention"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/dropout_prevention", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_dropout_prevention","s":"ativo","d":"Dropout Prevention","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_dropout_prevention"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
