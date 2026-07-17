#!/usr/bin/env python3
"""Asch Experimento"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/asch_experimento", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__asch_experimento","s":"ativo","d":"Asch Experimento","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__asch_experimento"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
