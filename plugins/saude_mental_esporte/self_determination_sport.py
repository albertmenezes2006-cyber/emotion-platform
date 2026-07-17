#!/usr/bin/env python3
"""Self Determination Sport"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/self_determination_sport", tags=["saude_mental_esporte"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_espor_self_determination_sport","s":"ativo","d":"Self Determination Sport","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_espor_self_determination_sport"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
