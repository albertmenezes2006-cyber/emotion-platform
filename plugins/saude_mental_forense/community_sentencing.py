#!/usr/bin/env python3
"""Community Sentencing"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/community_sentencing", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_community_sentencing","s":"ativo","d":"Community Sentencing","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_community_sentencing"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
