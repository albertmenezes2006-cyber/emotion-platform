#!/usr/bin/env python3
"""Identity Exploration"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/identity_exploration", tags=["saude_mental_adolescencia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_adole_identity_exploration","s":"ativo","d":"Identity Exploration","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_adole_identity_exploration"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
