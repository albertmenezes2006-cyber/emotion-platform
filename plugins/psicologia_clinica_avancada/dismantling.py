#!/usr/bin/env python3
"""Dismantling"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/dismantling", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_dismantling","s":"ativo","d":"Dismantling","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_dismantling"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
