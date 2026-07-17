#!/usr/bin/env python3
"""Safe Messaging Guidelines2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/safe_messaging_guidelines2", tags=["saude_mental_midia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_midia_safe_messaging_guidelines","s":"ativo","d":"Safe Messaging Guidelines2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_midia_safe_messaging_guidelines"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
