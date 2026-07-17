#!/usr/bin/env python3
"""Make The Connection"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/make_the_connection", tags=["saude_mental_militar"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_milit_make_the_connection","s":"ativo","d":"Make The Connection","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_milit_make_the_connection"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
