#!/usr/bin/env python3
"""Locker Room Culture"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/locker_room_culture", tags=["saude_mental_esporte"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_espor_locker_room_culture","s":"ativo","d":"Locker Room Culture","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_espor_locker_room_culture"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
