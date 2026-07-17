#!/usr/bin/env python3
"""Gun Access Veterans"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/gun_access_veterans", tags=["saude_mental_militar"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_milit_gun_access_veterans","s":"ativo","d":"Gun Access Veterans","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_milit_gun_access_veterans"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
