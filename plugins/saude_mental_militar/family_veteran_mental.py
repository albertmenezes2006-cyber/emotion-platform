#!/usr/bin/env python3
"""Family Veteran Mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/family_veteran_mental", tags=["saude_mental_militar"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_milit_family_veteran_mental","s":"ativo","d":"Family Veteran Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_milit_family_veteran_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
