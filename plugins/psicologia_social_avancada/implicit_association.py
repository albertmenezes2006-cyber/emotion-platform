#!/usr/bin/env python3
"""Implicit Association"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/implicit_association", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__implicit_association","s":"ativo","d":"Implicit Association","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__implicit_association"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
