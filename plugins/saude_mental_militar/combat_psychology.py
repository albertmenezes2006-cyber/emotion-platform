#!/usr/bin/env python3
"""Combat Psychology"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/combat_psychology", tags=["saude_mental_militar"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_milit_combat_psychology","s":"ativo","d":"Combat Psychology","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_milit_combat_psychology"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
