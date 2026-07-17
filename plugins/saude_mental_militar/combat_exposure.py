#!/usr/bin/env python3
"""Combat Exposure"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/combat_exposure", tags=["saude_mental_militar"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_milit_combat_exposure","s":"ativo","d":"Combat Exposure","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_milit_combat_exposure"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
