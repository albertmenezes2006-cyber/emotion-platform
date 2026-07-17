#!/usr/bin/env python3
"""Sport Psychology2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/sport_psychology2", tags=["saude_mental_esporte"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_espor_sport_psychology2","s":"ativo","d":"Sport Psychology2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_espor_sport_psychology2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
