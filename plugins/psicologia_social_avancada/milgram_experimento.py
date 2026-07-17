#!/usr/bin/env python3
"""Milgram Experimento"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/milgram_experimento", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__milgram_experimento","s":"ativo","d":"Milgram Experimento","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__milgram_experimento"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
