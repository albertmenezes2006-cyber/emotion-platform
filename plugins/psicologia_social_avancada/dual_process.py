#!/usr/bin/env python3
"""Dual Process"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/dual_process", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__dual_process","s":"ativo","d":"Dual Process","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__dual_process"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
