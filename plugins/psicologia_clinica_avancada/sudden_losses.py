#!/usr/bin/env python3
"""Sudden Losses"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/sudden_losses", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_sudden_losses","s":"ativo","d":"Sudden Losses","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_sudden_losses"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
