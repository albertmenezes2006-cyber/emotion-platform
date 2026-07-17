#!/usr/bin/env python3
"""Waitlist Control"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/waitlist_control", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_waitlist_control","s":"ativo","d":"Waitlist Control","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_waitlist_control"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
