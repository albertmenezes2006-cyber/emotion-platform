#!/usr/bin/env python3
"""Online Connection"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/online_connection", tags=["saude_mental_midia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_midia_online_connection","s":"ativo","d":"Online Connection","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_midia_online_connection"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
