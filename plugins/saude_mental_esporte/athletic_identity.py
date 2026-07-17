#!/usr/bin/env python3
"""Athletic Identity"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/athletic_identity", tags=["saude_mental_esporte"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_espor_athletic_identity","s":"ativo","d":"Athletic Identity","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_espor_athletic_identity"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
